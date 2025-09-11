# assurance/exception/__init__.py

"""
A package providing a structured hierarchy of exceptions for the `assurance` project.

This package defines a base `AssuranceException` from which all other custom
exceptions in the project should inherit. This allows for a clean and
consistent way to handle exceptions across different modules and layers
of the application.

The package includes specific validation exceptions for common data types,
such as `RankValidationException` and `IdValidationException`, promoting
predictable error handling and clear communication of validation failures.
"""

from assurance_exception import AssuranceException
from .invalid_rank import RankValidationException
from .invalid_id import IdValidationException
from .invalid_request import RequestValidationException
from .invalid_name import NameValidationException

# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "assurance.exception"

# Export control - only what belongs in public API
__all__ = [
    # Core classes
    "AssuranceException",
    "RankValidationException",
    "IdValidationException",
    "RequestValidationException",
    "NameValidationException",

    # Package metadata and utilities
    "__version__",
    "__author__",
    "package_info",
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