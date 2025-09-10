from . import coord
from . import scalar
from . import vector

from .coord_validation_execption import CoordValidationException
from .scalar_validation_exception import ScalarValidationException
from .vector_validation_exception import VectorValidationException


# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "geometry_exception_pkg"


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
    "CoordValidationException",
    "ScalarValidationException",
    "VectorValidationException",

    "__version__",
    "__author__",
    "package_info"
]