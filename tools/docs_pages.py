"""Write the documentation site's two pages from the schema: docs/fields.md and docs/lists.md.

Every field and every list value has an anchor on these pages, named by its id, so an id can point at its row.

    uv run python tools/docs_pages.py
"""
from pathlib import Path

from linkml_runtime.utils.schemaview import SchemaView

ROOT = Path(__file__).resolve().parent.parent
SCHEMA = ROOT / "src" / "t2t_data_model" / "schema" / "t2t_data_model.yaml"
DOCS = ROOT / "docs"
VIEW = SchemaView(str(SCHEMA))


def cell(text):
    return (text or "").replace("|", "\\|").replace("\n", "<br>")


def list_id(enum_name):
    return Path(VIEW.get_enum(enum_name).enum_uri).name


def list_link(slot):
    if slot.range in VIEW.all_enums():
        enum = VIEW.get_enum(slot.range)
        return f"[{cell(enum.title)}](lists.md#{list_id(slot.range)})"
    if slot.any_of:
        return "The list of its Contaminant Type"
    return ""


def group_title(group):
    return VIEW.get_slot(VIEW.get_class(group).slots[0]).title.split(" 1 ")[0]


HEAD = ["| CDM-ID | Field | Type | Values list | Values | Definition |", "|---|---|---|---|---|---|"]


def field_row(name):
    s = VIEW.get_slot(name)
    return (f'| <span id="{name}"></span>{s.annotations["cdm_id"].value} | {cell(s.title)} '
            f'| {s.annotations["type"].value}<br><small>{cell(s.annotations["data_format"].value)}</small> '
            f'| {list_link(s)} '
            f'| {"several" if s.multivalued else "one"} | {cell(s.description)} |')


def fields_page():
    spec = VIEW.get_class("Specification").slots
    groups = [VIEW.get_slot(n).range for n in spec if VIEW.get_slot(n).range in VIEW.all_classes()]
    lines = ["# Fields", "",
             ("The Specifications fields of the Common Data Model for Textile to Textile Recycling: first the fields "
              "a record holds once, then each group that repeats, each in CDM-ID order. Type is what a field holds: "
              "a Code is one value's code from its list, a Link points to a document; the model's own wording for "
              "the format is beneath it."), "",
             "## Specification", "", *HEAD,
             *[field_row(n) for n in spec if VIEW.get_slot(n).range not in VIEW.all_classes()], ""]
    for group in groups:
        title = group_title(group)
        lines += [f"## {title}", "",
                  (f"Repeats: a record can hold several {title} entries, each with these fields. "
                   "The 1 in a field's name marks that it repeats."), "",
                  *HEAD, *[field_row(n) for n in VIEW.get_class(group).slots], ""]
    lines += ["## Rules", ""] + [f"- {r.description}" for r in VIEW.get_class("Contaminant").rules] + [
        "- A contaminant with a Contaminant Type and no Contaminant Name covers every contaminant of that type.",
        "- Percentages (520.10, 650.20) are written 0–100.",
        "- A document is given as a link to the file.", ""]
    return "\n".join(lines)


def used_by():
    users = {}
    for s in VIEW.all_slots().values():
        for rng in [s.range] + [a.range for a in (s.any_of or [])]:
            if rng in VIEW.all_enums():
                users.setdefault(rng, []).append(f"[{s.annotations['cdm_id'].value} {s.title}](fields.md#{s.name})")
    return users


def lists_page():
    users = used_by()
    lines = ["# Values lists", "",
             ("Each list as published: a value's code is what a record holds, its label what people see. "
              "Each list is also published as SKOS (`.ttl`) and CSV."), ""]
    for name, enum in VIEW.all_enums().items():
        lid = list_id(name)
        lines += [f"## {enum.title} {{#{lid}}}", "",
                  (f"Used by {', '.join(users.get(name, []))}. "
                   f"Download: [SKOS](schema/lists/{lid}.ttl) · [CSV](schema/lists/{lid}.csv)"), "",
                  "| Code | Label | Definition |", "|---|---|---|"]
        for code, pv in enum.permissible_values.items():
            label = cell(pv.title) + (" *(retired)*" if pv.deprecated else "")
            lines.append(f'| <span id="{lid}-{code}"></span>`{code}` | {label} | {cell(pv.description)} |')
        lines.append("")
    return "\n".join(lines)


def main():
    (DOCS / "fields.md").write_text(fields_page())
    (DOCS / "lists.md").write_text(lists_page())
    print("docs/fields.md, docs/lists.md")


if __name__ == "__main__":
    main()
