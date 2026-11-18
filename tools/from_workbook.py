"""Build the release's sources from the CDM workbook (Fields + Values Lists tabs).

Writes the LinkML schema (src/t2t_data_model/schema/) and one SKOS concept scheme and one CSV per values list
(src/t2t_data_model/lists/). Scope: the
Specifications fields, CDM-ID 400–660. Names, definitions and descriptions are copied as written; a value's label
and a field's name lose only the whitespace around them.

A value's code is issued once and never changes: the list CSVs already in the repo are the register. A value whose
label is no longer in the workbook stops the build; reword its label in its list CSV (the code stays), or retire it in
RETIRED. See CONTRIBUTING.md.

    uv run python tools/from_workbook.py <workbook.xlsx>
"""
import csv
import re
import sys
from pathlib import Path

import openpyxl
import yaml
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import DCTERMS, OWL, RDF, SKOS

ROOT = Path(__file__).resolve().parent.parent / "src" / "t2t_data_model"
BASE = "https://texroad-foundation.github.io/t2t-data-model/"
REPO = "https://github.com/texroad-foundation/t2t-data-model"
PUBLISHER = "https://www.texroad.org"  # the TEXroad Foundation
VERSION = "0.1.0"
LICENSE = "https://creativecommons.org/licenses/by/4.0/"
T2T = Namespace(BASE)

# The workbook's list name → the list's id. An id is fixed once published; the name is the list's label.
LISTS = {
    "Material Source": "material_source",
    "Color Generic": "color_generic",
    "Fiber Composition Name": "fiber_composition_name",
    "Fiber Composition Threshold": "fiber_composition_threshold",
    "Contaminant Type": "contaminant_type",
    "Contaminant Type > Coatings and finishes": "contaminant_coatings_and_finishes",
    "Contaminant Type > Dyes and pigments": "contaminant_dyes_and_pigments",
    "Contaminant Type > Soft trims and prints": "contaminant_soft_trims_and_prints",
    "Contaminant Type > Hard trims": "contaminant_hard_trims",
    "Contaminant Type > Other materials": "contaminant_other_materials",
    "Contaminant Amount Unit": "contaminant_amount_unit",
    "Contaminant Threshold": "contaminant_threshold",
    "Contaminant Check": "contaminant_check",
    "Format": "format",
    "Physical Property Name": "physical_property_name",
    "Physical Property Unit": "physical_property_unit",
    "Fabric Construction": "fabric_construction",
}
# A Contaminant Type value → the list its Contaminant Name is chosen from. Fibers reads the fibre list (the workbook's
# "(See Fiber Composition)"); the others read their own list.
NAME_LIST_BY_TYPE = {
    "fibers": "fiber_composition_name",
    "coatings_and_finishes": "contaminant_coatings_and_finishes",
    "dyes_and_pigments": "contaminant_dyes_and_pigments",
    "soft_trims_and_prints": "contaminant_soft_trims_and_prints",
    "hard_trims": "contaminant_hard_trims",
    "other_materials": "contaminant_other_materials",
}
ADDED_LISTS = {"yes_no": ("Yes / No", ["Yes", "No"])}  # 530.40 and 650.00 select Yes or No; the tab holds no list
# Reading aids in the workbook, not values: "All" is a contaminant row with a type and no name; Fibers is the rule above.
NOT_VALUES = {"All", "(See Fiber Composition)"}
# A retired value: list id → {code: the code that replaces it, or None}. It stays published, marked deprecated.
RETIRED = {}
FIRST_CODES = {"∆E": "delta_e", "mL/g": "ml_per_g", "dL/g": "dl_per_g", "g/cm^3": "g_per_cm3", "%": "percent"}

# CDM-ID → (field id, values list, several values). The field id is the Data Field Name without its repeat number,
# plural where the field holds several values (LinkML's convention).
FIELDS = {
    "400.00": ("material_sources", "material_source", True),
    "500.00": ("internal_product_name", None, False),
    "510.00": ("color_generic", "color_generic", False),
    "520.00": ("fiber_composition_name", "fiber_composition_name", False),
    "520.10": ("fiber_composition_value", None, False),
    "520.20": ("fiber_composition_threshold", "fiber_composition_threshold", False),
    "530.00": ("contaminant_type", "contaminant_type", False),
    "530.10": ("contaminant_name", None, False),  # its list depends on 530.00 (NAME_LIST_BY_TYPE)
    "530.20": ("contaminant_amount", None, False),
    "530.21": ("contaminant_amount_unit", "contaminant_amount_unit", False),
    "530.22": ("contaminant_threshold", "contaminant_threshold", False),
    "530.30": ("contaminant_check", "contaminant_check", False),
    "530.40": ("contaminant_hazardous_substance", "yes_no", False),
    "530.41": ("contaminant_sds", None, False),
    "530.42": ("contaminant_explanation", None, False),
    "530.43": ("contaminant_evidence", None, False),
    "600.00": ("format", "format", False),
    "600.10": ("physical_property_name", "physical_property_name", False),
    "600.20": ("physical_property_value", None, False),
    "600.21": ("physical_property_unit", "physical_property_unit", False),
    "600.22": ("physical_property_verification_method", None, False),
    "600.30": ("fabric_construction", "fabric_construction", False),
    "650.00": ("recycled_content_in_outputs", "yes_no", False),
    "650.10": ("recycled_content_source", "material_source", False),
    "650.20": ("recycled_content_value", None, False),
    "660.00": ("certificate_of_analysis", None, False),
}
# The groups that repeat together (a "1" in the Data Field Name): group class → (slot on Specification, its fields).
GROUPS = {
    "FiberComposition": ("fiber_compositions", ["520.00", "520.10", "520.20"]),
    "Contaminant": ("contaminants", ["530.00", "530.10", "530.20", "530.21", "530.22", "530.30",
                                     "530.40", "530.41", "530.42", "530.43"]),
    "PhysicalProperty": ("physical_properties", ["600.10", "600.20", "600.21", "600.22"]),
    "RecycledContent": ("recycled_contents", ["650.10", "650.20"]),
}
GROUP_LABELS = {"FiberComposition": "Fiber Composition", "Contaminant": "Contaminant",
                "PhysicalProperty": "Physical Property", "RecycledContent": "Recycled Content"}
# The documents a hazardous substance needs: the fields whose definitions say "Required when … 'yes'".
HAZARD_DOCUMENTS = ("contaminant_sds", "contaminant_explanation")
# The workbook's machine-readable data format (the column after Data Format) → what the schema says of the field.
FORMATS = {
    "Code (from values list)": {},
    "Text": {"range": "string"},
    "Text (multi-line)": {"range": "string"},
    "Decimal number": {"range": "decimal"},
    "Decimal number (0 or more)": {"range": "decimal", "minimum_value": 0},
    "Percentage (0–100)": {"range": "decimal", "minimum_value": 0, "maximum_value": 100, "unit": {"symbol": "%"}},
    "Link to document": {"range": "uri"},
}
CSV_COLUMNS = ["id", "code", "label", "definition", "retired", "replaced_by"]


def label_of(value):
    return re.sub(r"\s+", " ", str(value).replace("\xa0", " ")).strip() if value is not None else ""


def text_of(value):
    """A definition or description as written: only the whitespace at its ends goes."""
    return str(value).replace("\xa0", " ").strip() if value is not None else ""


def first_code(label):
    if label in FIRST_CODES:
        return FIRST_CODES[label]
    text = label.lower().replace("&", "and").replace("%", "percent")
    return re.sub(r"[^a-z0-9]+", "_", text).strip("_")


def register(list_id):
    path = ROOT / "lists" / f"{list_id}.csv"
    if not path.exists():
        return []
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def with_codes(list_id, rows):
    """Each workbook value with its code from the register; a new value gets its first code."""
    published = register(list_id)
    code_by_label = {r["label"]: r["code"] for r in published}
    retired = RETIRED.get(list_id, {})
    values = []
    for label, definition in rows:
        code = code_by_label.get(label) or first_code(label)
        values.append({"code": code, "label": label, "definition": definition})
    codes = [v["code"] for v in values]
    assert len(codes) == len(set(codes)), f"{list_id}: two values share a code"
    back = set(codes) & set(retired)
    assert not back, f"{list_id}: retired codes are in the workbook again: {sorted(back)}"
    gone = [r for r in published if r["code"] not in codes and r["code"] not in retired]
    assert not gone, (f"{list_id}: published values no longer in the workbook: "
                      f"{[(r['code'], r['label']) for r in gone]}. Reword the label in lists/{list_id}.csv (the code "
                      f"stays) or retire the code in RETIRED.")
    for r in published:
        if r["code"] in retired:
            values.append({"code": r["code"], "label": r["label"], "definition": r["definition"],
                           "retired": True, "replaced_by": retired[r["code"]]})
    return values


def read_lists(sheet):
    rows = {}
    for row in sheet.iter_rows(min_row=2, values_only=True):
        name, label, definition = label_of(row[0]), label_of(row[1]), text_of(row[2])
        if name in LISTS and label and label not in NOT_VALUES:
            rows.setdefault(LISTS[name], {"label": name, "rows": []})["rows"].append((label, definition))
    for list_id, (name, labels) in ADDED_LISTS.items():
        rows[list_id] = {"label": name, "rows": [(label, "") for label in labels]}
    assert set(rows) == set(LISTS.values()) | set(ADDED_LISTS), "a list is missing from the workbook"
    return {list_id: {"label": r["label"], "values": with_codes(list_id, r["rows"])} for list_id, r in rows.items()}


def columns(sheet):
    """The Fields tab's columns by header; the machine-readable format is the header starting "Data Format ("."""
    header = [label_of(c) for c in next(sheet.iter_rows(max_row=1, values_only=True))]
    col = {name: header.index(name) for name in ("Category", "CDM-ID", "Data Field Name", "Data Format", "Definition")}
    col["type"] = next(i for i, name in enumerate(header) if name.startswith("Data Format ("))
    return col


def read_fields(sheet):
    col, fields = columns(sheet), {}
    for row in sheet.iter_rows(min_row=2, values_only=True):
        if label_of(row[col["Category"]]) == "Specifications" and row[col["CDM-ID"]] is not None:
            fields[f"{float(row[col['CDM-ID']]):.2f}"] = {
                "name": label_of(row[col["Data Field Name"]]), "data_format": label_of(row[col["Data Format"]]),
                "type": label_of(row[col["type"]]), "definition": text_of(row[col["Definition"]])}
    assert set(fields) == set(FIELDS), f"fields differ from the workbook: {set(fields) ^ set(FIELDS)}"
    for cdm_id, field in fields.items():
        assert field["type"] in FORMATS, f"{cdm_id}: unknown data format {field['type']!r}"
        has_list = FIELDS[cdm_id][1] is not None or cdm_id == "530.10"
        assert has_list == (field["type"] == "Code (from values list)"), f"{cdm_id}: a Code field takes a list"
    return fields


def concept(list_id, code):
    return f"{BASE}lists/{list_id}/{code}"


def live_codes(values):
    return [v["code"] for v in values if not v.get("retired")]


def permissible_value(list_id, v):
    pv = {"title": v["label"], "meaning": concept(list_id, v["code"])}
    if v["definition"]:
        pv["description"] = v["definition"]
    if v.get("retired"):
        pv["deprecated"] = "Retired."
        if v.get("replaced_by"):
            pv["deprecated_element_has_exact_replacement"] = concept(list_id, v["replaced_by"])
    return pv


def enum(list_id, values):
    return {
        "title": values["label"],
        "enum_uri": f"{BASE}lists/{list_id}",
        "permissible_values": {v["code"]: permissible_value(list_id, v) for v in values["values"]},
    }


def enum_name(list_id):
    return "".join(part.capitalize() for part in list_id.split("_"))


def slot(cdm_id, field):
    slot_id, list_id, several = FIELDS[cdm_id]
    data = {"title": field["name"], "slot_uri": f"t2t:{slot_id}"}
    if field["definition"]:
        data["description"] = field["definition"]
    if list_id:
        data["range"] = enum_name(list_id)
    elif cdm_id == "530.10":
        data["any_of"] = [{"range": enum_name(l)} for l in NAME_LIST_BY_TYPE.values()]
    data |= FORMATS[field["type"]]
    if several:
        data["multivalued"] = True
    data["annotations"] = {"cdm_id": cdm_id, "type": field["type"], "data_format": field["data_format"]}
    return slot_id, data


def contaminant_rules(lists):
    type_label = {v["code"]: v["label"] for v in lists["contaminant_type"]["values"]}
    rules = [
        {"description": f"A {type_label[t]} contaminant is named from the {lists[l]['label']} list.",
         "preconditions": {"slot_conditions": {"contaminant_type": {"equals_string": t}}},
         "postconditions": {"slot_conditions": {"contaminant_name": {
             "equals_string_in": [v["code"] for v in lists[l]["values"]], "required": False}}}}
        for t, l in NAME_LIST_BY_TYPE.items()
    ]
    rules.append({
        "description": "A hazardous substance needs its SDS and explanation (530.41, 530.42).",
        "preconditions": {"slot_conditions": {"contaminant_hazardous_substance": {"equals_string": "yes"}}},
        "postconditions": {"slot_conditions": {s: {"required": True} for s in HAZARD_DOCUMENTS}},
    })
    return rules


def schema(fields, lists):
    slots = dict(slot(cdm_id, field) for cdm_id, field in fields.items())
    grouped = {c for _, ids in GROUPS.values() for c in ids}
    classes = {"Specification": {
        "tree_root": True,
        "description": "A batch's output specification or a technology's input requirements (CDM-ID 400 to 660).",
        "slots": [],
    }}
    for group, (group_slot, ids) in GROUPS.items():
        slots[group_slot] = {"range": group, "multivalued": True, "inlined_as_list": True}
        classes[group] = {"description": f"One {GROUP_LABELS[group]} entry, repeated as a group "
                                         f"(the fields with a 1 in their name).",
                          "slots": [FIELDS[c][0] for c in ids]}
    first_of = {ids[0]: group_slot for group_slot, ids in GROUPS.values()}
    for cdm_id in fields:  # in CDM-ID order; a group sits where its first field does
        if cdm_id in first_of:
            classes["Specification"]["slots"].append(first_of[cdm_id])
        elif cdm_id not in grouped:
            classes["Specification"]["slots"].append(FIELDS[cdm_id][0])
    classes["Contaminant"]["rules"] = contaminant_rules(lists)
    return {
        "id": BASE,
        "name": "t2t_data_model",
        "title": "Common Data Model for Textile to Textile Recycling — Specifications",
        "description": "The Specifications fields (CDM-ID 400–660) of the Common Data Model for Textile to Textile "
                       "Recycling, and their values lists.",
        "version": VERSION,
        "license": LICENSE,
        "created_by": PUBLISHER,
        "see_also": [REPO],
        "in_language": "en",
        "keywords": ["textile recycling", "textile to textile", "feedstock", "specification", "contaminant"],
        "prefixes": {"t2t": BASE, "linkml": "https://w3id.org/linkml/"},
        "default_prefix": "t2t",
        "default_range": "string",
        "imports": ["linkml:types"],
        "classes": classes,
        "slots": slots,
        "enums": {enum_name(l): enum(l, v) for l, v in lists.items()},
    }


def skos(list_id, values):
    g = Graph()
    g.bind("skos", SKOS), g.bind("dct", DCTERMS), g.bind("t2t", T2T), g.bind("owl", OWL)
    scheme = URIRef(f"{BASE}lists/{list_id}")
    g.add((scheme, RDF.type, SKOS.ConceptScheme))
    g.add((scheme, DCTERMS.title, Literal(values["label"], lang="en")))
    g.add((scheme, OWL.versionInfo, Literal(VERSION)))
    g.add((scheme, DCTERMS.license, URIRef(LICENSE)))
    g.add((scheme, DCTERMS.publisher, URIRef(PUBLISHER)))
    g.add((scheme, DCTERMS.isPartOf, URIRef(BASE)))
    parent_type = next((t for t, l in NAME_LIST_BY_TYPE.items() if l == list_id and l.startswith("contaminant_")), None)
    for v in values["values"]:
        c = URIRef(concept(list_id, v["code"]))
        g.add((c, RDF.type, SKOS.Concept))
        g.add((c, SKOS.prefLabel, Literal(v["label"], lang="en")))
        g.add((c, SKOS.notation, Literal(v["code"])))
        g.add((c, SKOS.inScheme, scheme))
        if v["definition"]:
            g.add((c, SKOS.definition, Literal(v["definition"], lang="en")))
        if parent_type:
            g.add((c, SKOS.broader, URIRef(f"{BASE}lists/contaminant_type/{parent_type}")))
        if v.get("retired"):
            g.add((c, OWL.deprecated, Literal(True)))
            if v.get("replaced_by"):
                g.add((c, DCTERMS.isReplacedBy, URIRef(concept(list_id, v["replaced_by"]))))
        else:
            g.add((c, SKOS.topConceptOf, scheme))
            g.add((scheme, SKOS.hasTopConcept, c))
    return g


def write_list(list_id, values):
    skos(list_id, values).serialize(ROOT / "lists" / f"{list_id}.ttl", format="turtle")
    with open(ROOT / "lists" / f"{list_id}.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, CSV_COLUMNS)
        w.writeheader()
        for v in values["values"]:
            w.writerow({"id": concept(list_id, v["code"]), "code": v["code"], "label": v["label"],
                        "definition": v["definition"], "retired": "yes" if v.get("retired") else "",
                        "replaced_by": v.get("replaced_by") or ""})


def main(workbook):
    wb = openpyxl.load_workbook(workbook, data_only=True)
    fields, lists = read_fields(wb["Common Data Model Fields"]), read_lists(wb["Values Lists"])
    for folder in ("schema", "lists"):
        (ROOT / folder).mkdir(exist_ok=True)
    built = schema(fields, lists)
    (ROOT / "schema" / "t2t_data_model.yaml").write_text(
        yaml.safe_dump(built, sort_keys=False, allow_unicode=True, width=120))
    for list_id, values in lists.items():
        write_list(list_id, values)
    stale = {p.stem for p in (ROOT / "lists").glob("*.csv")} - set(lists)
    assert not stale, f"list files with no list: {stale}"
    print(f"{len(fields)} fields, {len(lists)} lists, {sum(len(v['values']) for v in lists.values())} values")


if __name__ == "__main__":
    main(sys.argv[1])
