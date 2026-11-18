"""The schema's enums and the published SKOS lists say the same thing: every value, its code, its label, its id."""
from pathlib import Path

from linkml_runtime.utils.schemaview import SchemaView
from rdflib import Graph, URIRef
from rdflib.namespace import RDF, SKOS

PACKAGE = Path(__file__).resolve().parent.parent / "src" / "t2t_data_model"
VIEW = SchemaView(str(PACKAGE / "schema" / "t2t_data_model.yaml"))


def scheme(enum):
    g = Graph().parse(PACKAGE / "lists" / f"{Path(enum.enum_uri).name}.ttl")
    return g, URIRef(enum.enum_uri)


def test_every_enum_is_a_published_list_with_the_same_values():
    for enum in VIEW.all_enums().values():
        g, uri = scheme(enum)
        concepts = set(g.subjects(SKOS.inScheme, uri))
        assert {URIRef(pv.meaning) for pv in enum.permissible_values.values()} == concepts, enum.name
        for code, pv in enum.permissible_values.items():
            concept = URIRef(pv.meaning)
            assert str(g.value(concept, SKOS.notation)) == code, (enum.name, code)
            assert str(g.value(concept, SKOS.prefLabel)) == pv.title, (enum.name, code)


def test_every_list_field_names_a_list_that_exists():
    for slot in VIEW.all_slots().values():
        if slot.range in VIEW.all_enums():
            assert (PACKAGE / "lists" / f"{Path(VIEW.get_enum(slot.range).enum_uri).name}.ttl").exists(), slot.name


def test_every_field_carries_its_cdm_id():
    grouping = {"fiber_compositions", "contaminants", "physical_properties", "recycled_contents"}
    for slot in VIEW.all_slots().values():
        if slot.name not in grouping:
            assert "cdm_id" in slot.annotations, slot.name


def test_a_contaminant_list_sits_under_its_type():
    g = Graph().parse(PACKAGE / "lists" / "contaminant_hard_trims.ttl")
    broader = set(g.objects(None, SKOS.broader))
    assert len(broader) == 1 and str(broader.pop()).endswith("/contaminant_type/hard_trims")
    assert all(g.value(c, SKOS.inScheme) for c in g.subjects(RDF.type, SKOS.Concept))
