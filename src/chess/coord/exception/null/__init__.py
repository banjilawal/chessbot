"""
chess.coord.exception.null package

PURPOSE:
   Puts exceptions to higly cohesive witl null Coords

CORE CLASSES:
    NullCoordException
    NullRowException
    NullColumnException
    NullCoordStackException

USAGE:
    >>>

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""


from .coord_null import NullCoordException
from .row_null import NullRowException
from .col_null import NullColumnException
from .null_coord_stack import NullCoordStackException


# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.coord.exception.null"


__all__ = [
    # Core Packages
    "NullCoordException",
    "NullRowException",
    "NullColumnException",
    "NullCoordStackException",


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
