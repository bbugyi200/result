"""Contains the result package's main entry point."""

import sys
from typing import Sequence


def main(argv: Sequence[str] = None) -> int:
    """Main entry point."""
    if argv is None:  # pragma: no cover
        argv = sys.argv

    return 0
