
from .row_above_bounds import RowAboveBoundsException
from .row_below_bounds import RowBelowBoundsException
from .column_below_bounds import ColumnBelowBoundsException
from .coord_above_bonds import ColumnAboveBoundsException
from .coord_null import NullCoordException
from .row_null import NullRowException
from .column_null import NullColumnException

NullRow = NullRowException
NullCoord = NullCoordException
NullColumn = NullColumnException

RowBelowBounds = RowBelowBoundsException
RowAboveBounds = RowAboveBoundsException
ColumnBelowBounds = ColumnBelowBoundsException
ColumnAboveBounds = ColumnAboveBoundsException


# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "geometry_exception_coord.pkg"


# Organic utility function for package info
def package_info() -> dict:
    """Return basic package information."""
    return {
        "name": __package_name__,
        "version": __version__,
        "author": __author__,
        "exports": __all__
    }


__all__ = [
    # Core Packages
    "NullCoordException",
    "NullRowException",
    "NullColumnException",
    "RowBelowBoundsException",
    "RowAboveBoundsException",
    "ColumnBelowBoundsException",
    "ColumnAboveBoundsException",

    # Aliases
    "NullRow",
    "NullCoord",
    "NullColumn",
    "RowBelowBounds",
    "RowAboveBounds",
    "ColumnBelowBounds",
    "ColumnAboveBounds",

    "__version__",
    "__author__",
    "package_info"
]