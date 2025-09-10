
from .scalar_null import NullScalarException
from .scalar_below_bounds import ScalarBelowLowerBoundException
from .scalar_above_bounds import ScalarAboveUpperBoundException


NullScalar = NullScalarException
ScalarBelowBounds = ScalarBelowLowerBoundException
ScalarAboveBounds= ScalarAboveUpperBoundException


# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "geometry_exception_scalar_pkg"


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
    "NullScalarException",
    "ScalarBelowLowerBoundException",
    "ScalarAboveUpperBoundException",

    # Aliases
    "NullScalar",
    "ScalarBelowBounds",
    "ScalarAboveBounds",


    "__version__",
    "__author__",
    "package_info"
]