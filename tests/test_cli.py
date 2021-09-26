"""Tests the result.cli module."""

from result.cli import main


def test_main() -> None:
    """Tests main() function."""
    assert main([""]) == 0
