import pytest
from python.helpers.files import is_full_json_template


def test_handles_missing_trailing_newline():
    text = "```json\n{\"a\": 1}```"
    assert is_full_json_template(text)


def test_handles_trailing_newline():
    text = "```json\n{\"a\": 1}\n```"
    assert is_full_json_template(text)
