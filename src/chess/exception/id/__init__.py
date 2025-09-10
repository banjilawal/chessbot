from .null_id import IdNullException
from .negative_id import NegativeIdException

IdNull = IdNullException
NegativeId = NegativeIdException


# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "exception"


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
    'NullNameException',
    'BlankNameException',
    'NullName',
    'BlankName',

    "__version__",
    "__author__",
    "package_info"
]
