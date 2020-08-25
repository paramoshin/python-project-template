"""Test cases for example."""
import pytest

from {{ cookiecutter.github_name }}.example import hello


def test_example(mock_example):
    s = hello("World")
    assert "Hello" in s
