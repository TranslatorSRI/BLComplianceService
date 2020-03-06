"""Test bl_compliance validator.py"""
from pathlib import Path
import pytest
import json
from bl_compliance.validator import validate_with_jsonschema, validate_with_kgx


biolink_json = Path(__file__).parent / 'resources' / 'biolink-compliant.json'
robokop_json = Path(__file__).parent / 'resources' / 'robokop.json'


def test_compliant_json_with_kgx():
    """
    Test bl compliant json with kgx validator
    """
    biolink_compliant = open(biolink_json, 'r')
    data = json.load(biolink_compliant)
    biolink_compliant.close()

    errors = validate_with_kgx(data)

    assert len(errors) == 1


def test_robokop_with_kgx():
    """
    Test robokop json with kgx validator
    """
    robokop = open(robokop_json, 'r')
    data = json.load(robokop)
    robokop.close()

    errors = validate_with_kgx(data)

    assert len(errors) > 0


@pytest.mark.skip(reason="test not implemented")
def test_val_with_jsonschema():
    """
    Test stub for testing validation with json schema
    """
    assert True
