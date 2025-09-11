import logging

from .exception import *
from .validators import *

from .throw_helper import ThrowHelper
from .error_handler import ErrorHandler
from .deployment_mode import Deployment
from .transaction_report import TransactionReport

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

    # Subpackages
    *exception.__all__,
    "exception",

    *validators.__all__,
    "validators",


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