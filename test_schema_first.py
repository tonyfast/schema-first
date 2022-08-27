import json
from pathlib import Path
from hypothesis import given
from hypothesis_jsonschema import from_schema
HERE = Path(__file__).parent

SCHEMA = HERE / "src" / "schema" / "my_schema_model.json"

from my_schema_project import get_item

@given(from_schema(json.loads(SCHEMA.read_text())))
def test_get_item(data):
    print(len(data))
    assert str(get_item(**data))