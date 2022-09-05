from pathlib import Path
from subprocess import check_call
import sys

import requests
from hatchling.builders.hooks.plugin.interface import BuildHookInterface


ROOT = Path(".").resolve()
SRC = ROOT / "src"
SCHEMA = SRC / "schema"
SCHEMASTORE = SRC / "schemastore"
MODELS = SRC / "my_schema_project" / "models"

SCHEMASTORE_URL = (
    "https://raw.githubusercontent.com/SchemaStore/schemastore/master/src/schemas/json/"
)

# Add `datamodel_code_generator` flags here
MY_SCHEMAS = {"my_schema_model.json": {"flags": []}}

# Add `datamodel_code_generator` flags here
SCHEMASTORE_SCHEMAS = {
    "github-workflow.json": {"flags": ["--allow-population-by-field-name"]}
}

ALL_SCHEMA = {**MY_SCHEMAS, **SCHEMASTORE_SCHEMAS}


class SchemaCodeGen(BuildHookInterface):
    PLUGIN_NAME = "hatch-schema-codegen"

    def initialize(self, version, build_data):
        L = get_logger()
        L.info("fetch schemastore schema")

        for schema in SCHEMASTORE_SCHEMAS.keys():
            SCHEMASTORE.mkdir(exist_ok=True)
            target = SCHEMASTORE / schema
            with target.open("w+") as file:
                r = requests.get(SCHEMASTORE_URL + schema)
                file.write(r.text)

        L.info("converting json schema to python")
        MODELS.mkdir(exist_ok=True)

        for path in [*SCHEMA.glob("*.json"), *SCHEMASTORE.glob("*.json")]:
            target = MODELS / path.with_suffix(".py").name
            flags = ALL_SCHEMA.get(path.name).get("flags")
            with target.open("w") as file:
                gen_models(path, file, flags)
            build_data["artifacts"].append("/" + str(target))

    def finalize(self, version, build_data, artifact_path):
        L = get_logger()
        L.info("delete schemastore schema")

        for f in SCHEMASTORE.glob("*.json"):
            f.unlink()

        SCHEMASTORE.rmdir()


def get_logger():
    import logging

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logging.basicConfig(level=logging.INFO)
    return logger


def gen_models(input: str, output: str, flags: list = []):
    check_call(
        [
            sys.executable,
            "-m",
            "datamodel_code_generator",
            "--input",
            input,
            *flags,
        ],
        stdout=output,
    )
