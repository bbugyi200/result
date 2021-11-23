"""A fully type-annotated Rust-like Result type for Python."""

from .result import Err, Ok, Result, return_lazy_result


__all__ = ["Err", "Ok", "Result", "return_lazy_result"]
__author__ = "Bryan M Bugyi"
__email__ = "bryanbugyi34@gmail.com"
__version__ = "0.2.0"
