"""

## ASSURANCE EXCEPTION
A package providing a structured hierarchy of exceptions for the `assurance` project.

This package defines a base `AssuranceException` from which all other custom
exceptions in the project should inherit. This allows for a clean and
consistent way to handle exceptions across different modules and layers
of the application.

The package includes specific validation exceptions for common data types,
such as `RankValidationException` and `IdValidationException`, promoting
predictable error handling and clear communication of validation failures.
"""


import logging

from .validators import *

from .throw_helper import ThrowHelper
from .error_handler import ErrorHandler
from .deployment_mode import Deployment
from .transaction_report import TransactionReport

from .exception import (
    AssuranceException,
    ConflictingEventStateException,
    EmptyConstructorException,
    EmptyResultConstructorException,
    EmptyEventOutcomeConstructorException,

)


log = logging.getLogger("chessbot")


# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "assurance"

# Export control - only what belongs in public API
__all__ = [
    # Core classes
    "ThrowHelper",
    "ErrorHandler",
    "Deployment",
    "TransactionReport",
    "AssuranceException",
    "ConflictingEventStateException",
    "EmptyConstructorException",
    "EmptyResultConstructorException",
    "EmptyEventOutcomeConstructorException",
    "HostageValidator",
    "IdValidator",
    "NameValidator",




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