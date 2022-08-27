from functools import partial
from io import StringIO
from logging import shutdown
from pathlib import Path
import os
import shlex
from subprocess import call, check_call
import sys
from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class SchemaCodeGen(BuildHookInterface):
    PLUGIN_NAME = "hatch-schema-codegen"

    def initialize(self, version, build_data):
        L = get_logger()
        WIN = os.name == "nt"
        L.info("converting json schema to python")
        ROOT = Path(self.root)
        SRC = ROOT / "src"
        SCHEMA = (SRC / "schema")
        MODELS = (SRC / "my_schema_project" / "models")
        MODELS.mkdir(exist_ok=True)

        for path in SCHEMA.glob("*.json"):
            target =(MODELS / path.with_suffix(".py").name)
            with target.open("w") as file:
                check_call([
                    sys.executable,
                    "-m", 
                    "datamodel_code_generator",
                    "--input", path
                    ], stdout=file)
            build_data["artifacts"].append(
                "/" + str(target)
            )


def get_logger():
    import logging

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logging.basicConfig(level=logging.INFO)
    return logger