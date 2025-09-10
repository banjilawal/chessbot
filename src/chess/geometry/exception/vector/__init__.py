
from .null_vector import NullVectorException
from .null_x_dim import NullXDimensionException
from .null_y_dim import NullYDimensionException

from .x_below_bounds import XBelowBoundsException
from .x_above_bounds import XAboveBoundsException

from .y_below_bounds import YBelowBoundsException
from .y_above_bounds import YAboveBoundsException


NullVector = NullVectorException
NullXDimension = NullXDimensionException
NullYDimension = NullYDimensionException

XBelowBounds = XBelowBoundsException
XAboveBounds = XAboveBoundsException

YBelowBounds = YBelowBoundsException
YAboveBounds = YAboveBoundsException


# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "geometry_exception_vector_pkg"


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
    "NullVectorException",
    "NullXDimensionException",
    "NullYDimensionException",

    "XBelowBoundsException",
    "XAboveBoundsException",

    "YBelowBoundsException",
    "YAboveBoundsException",

    # Aliases
    "NullVector",
    "NullXDimension",
    "NullYDimension",

    "XBelowBounds",
    "XAboveBounds",

    "YBelowBounds",
    "YAboveBounds",


    "__version__",
    "__author__",
    "package_info"
]