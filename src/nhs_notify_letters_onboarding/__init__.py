import importlib.resources
from typing import Any

import jsonschema
import yaml

ValidationError = jsonschema.ValidationError

_SCHEMA = None


def _get_schema() -> dict:
    global _SCHEMA
    if _SCHEMA is None:
        text = (
            importlib.resources.files("nhs_notify_lettersonboarding")
            .joinpath("schema.yaml")
            .read_text(encoding="utf-8")
        )
        _SCHEMA = yaml.safe_load(text)
    return _SCHEMA


def validate(instance: Any) -> None:
    """Validate a DocumentReference dict against the NHS Notify schema.

    Raises:
        jsonschema.ValidationError: if the payload is invalid.
    """
    jsonschema.validate(instance=instance, schema=_get_schema())
