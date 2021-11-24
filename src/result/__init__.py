"""A fully type-annotated Rust-like Result type for Python."""

import logging as _logging

from ._core import Err, LazyResult, Ok, Result, return_lazy_result


__all__ = ["Err", "LazyResult", "Ok", "Result", "return_lazy_result"]
__author__ = "Bryan M Bugyi"
__email__ = "bryanbugyi34@gmail.com"
__version__ = "0.2.1"

_logging.getLogger(__name__).addHandler(_logging.NullHandler())
