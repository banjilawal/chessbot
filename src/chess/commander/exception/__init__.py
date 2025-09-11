"""
Commander Exception ExceptionPackage

PURPOSE:
    Contains core commander exception classes and coordinate utilities.


CORE CLASSES:
    NullCommanderException
    CommandervalidationException


USAGE:
    >>>
    >>>

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

# Subpackage imports

# Core imports
from .null import NullCommanderException
from .invalid_commander import CommanderValidationException


# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.commander.exception"

# Export control - only what belongs in public API
__all__ = [
    # Core classes
    "NullCommanderException",
    "CommanderValidationException",

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