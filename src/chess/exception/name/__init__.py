"""
chess.exception.name Package

Purpose:
    Name exceptions are thrown during validation. More granular than regular string checks

Class:
    BlankNameException
    NullNameException
    ShortNameException
    LongNameException

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

from .blank_name_exception import BlankNameException
from .null_name_exception import NullNameException
from .short_name_exception import ShortNameException
from .long_name_exception import LongNameException

# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.exception.name"


__all__ = [
    "NullNameException",
    "BlankNameException",
    "ShortNameException",
    "LongNameException",

    "__version__",
    "__author__",
    "package_info"
]

# Organic utility function for package info
def package_info() -> dict:
    """Return basic package information."""
    return {
        "name": __package_name__,
        "version": __version__,
        "author": __author__,
        "exports": __all__
    }



