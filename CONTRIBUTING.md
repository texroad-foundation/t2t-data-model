# Contributing to t2t-data-model

Thank you for helping improve the Common Data Model for Textile to Textile Recycling. Please read our
[Code of Conduct](CODE_OF_CONDUCT.md).

## Comments and proposals

Use the [issue tracker][issues] to report a problem, ask a question, or propose a field or a value. Say which field
(by CDM-ID) or which list and value it concerns, and why. The TEXroad team reviews proposals with the model's authors;
an accepted change ships in the next release.

## How the model changes

The model's workbook is its source: a change is made there, then built into this repository with
`uv run python tools/from_workbook.py <workbook.xlsx>` and opened as a pull request, reviewed before it is merged.

- **Codes and ids never change.** A value keeps its code, and a field its id, for every later release. Rewording a
  label keeps its code: change the label in the list's CSV under `src/t2t_data_model/lists/` before building.
- **Nothing published is deleted.** A value that is no longer used is retired: it stays in its list, marked
  deprecated (`deprecated` in the schema, `owl:deprecated` in SKOS), with the value that replaces it where there is
  one (`deprecated_element_has_exact_replacement`, `dct:isReplacedBy`). Records that use it stay readable.
- **Versions** follow [semantic versioning](https://semver.org): a patch release changes wording only; a minor release
  adds fields or values, or retires values; a major release changes what an existing field or value means.
- `just test` must pass before a release; the records that check each rule are kept with the TEXroad team.

## LinkML

The schema follows the [LinkML](https://linkml.io/linkml) conventions: UpperCamelCase for classes and enums,
snake_case for fields, an enum for every values list. See the [LinkML schemas guide](https://linkml.io/linkml/schemas/index.html).

[issues]: https://github.com/texroad-foundation/t2t-data-model/issues/
