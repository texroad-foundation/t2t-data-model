# t2t-data-model

The Specifications fields (CDM-ID 400–660) of the **Common Data Model for Textile to Textile Recycling**, and their
values lists, in machine-readable form. The model is described in *Common Data Model for Textile to Textile
Recycling*, a follow-up document to PESCO-UP D2.1 and a deliverable from ECOSYSTEX Target Group 5.

Published by the [TEXroad Foundation](https://texroad.org). Documentation:
<https://texroad-foundation.github.io/t2t-data-model>

## What is published

| What | Standard | Where |
|---|---|---|
| The fields: name, CDM-ID, data format, definition, which repeat together, one value or several | [LinkML](https://linkml.io/linkml/) | [`src/t2t_data_model/schema/t2t_data_model.yaml`](src/t2t_data_model/schema/t2t_data_model.yaml) |
| The same fields as a table | CSV | [`src/t2t_data_model/fields/specifications.csv`](src/t2t_data_model/fields/specifications.csv) |
| Each values list: its values, their codes, labels and definitions | [SKOS](https://www.w3.org/TR/skos-reference/) concept schemes, and CSV | [`src/t2t_data_model/lists/`](src/t2t_data_model/lists/) |
| A validator for records | JSON Schema, generated from the LinkML schema | on the documentation site, `schema/t2t_data_model.schema.json` |

Names, definitions and descriptions are as the model publishes them.

## Reading the model

- **A field is identified** by its id (`https://texroad-foundation.github.io/t2t-data-model/contaminant_threshold`);
  its CDM-ID (`530.22`) is kept on it, so the document's references find it.
- **A field marked "Text (from values list)"** holds the code of one value of its list (`post_consumer_residential`);
  its label (`Post-consumer, Residential`) is what people see. Each list field takes one value; Material Source (400)
  repeats, so a record can name several sources.
- **Fields with a 1 in their name repeat as a group**: Fiber Composition (520), Contaminant (530), Physical
  Property (600.10–600.22) and Recycled Content (650.10–650.20).
- **Contaminant Name (530.10) is chosen from the list of its Contaminant Type (530.00)**; Fibers uses the Fiber
  Composition Name list. A contaminant with a type and no name covers every contaminant of that type.
- **A hazardous substance (530.40 = Yes)** needs its SDS and explanation (530.41, 530.42); evidence (530.43) is optional.
- **Percentages** (520.10, 650.20) are written 0–100.
- **A document** (530.41, 530.43, 660) is given as a link to the file.
- **A record holds only these fields**: the JSON Schema refuses a field it doesn't know, so a record that also carries
  other parts of the model (Entity Details, Batch Info) is validated part by part.
- **Codes never change**, and a retired value stays published, marked deprecated with its replacement (see
  [CONTRIBUTING.md](CONTRIBUTING.md)).

## Versions

Each release is tagged (`v0.1.0`) and listed in [CHANGELOG.md](CHANGELOG.md).

## Feedback

Comments and proposed changes are welcome as [issues](https://github.com/texroad-foundation/t2t-data-model/issues).

## Licence

[CC BY 4.0](LICENSE). Cite as in [CITATION.cff](CITATION.cff).

## For maintainers

The schema and lists are built from the model's workbook: `uv run python tools/from_workbook.py <workbook.xlsx>`.
`just test` checks the schema and that the lists and the schema agree; the records that check each rule live in a
separate repository. `just testdoc` previews the documentation. Built with
[linkml-project-copier](https://github.com/linkml/linkml-project-copier).
