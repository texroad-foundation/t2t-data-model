"""Data model package for t2t-data-model."""

from pathlib import Path
from .t2t_data_model import *  # noqa: F403

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "t2t_data_model.yaml"
