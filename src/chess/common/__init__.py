"""
Common Package - Objects used frequently and globally accross packages

PURPOSE:
    Contains commonly used objects and utilites

CORE CLASSES:
    Event, Result, GameColor, MousePlacementStatus

CONVENIENCE ALIASES:
    MousePlacement: Alias for MousePlacementStatus

USAGE:
    >>>
    >>>

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

# Subpackage imports
from .exception import *

# Import constants
from .config import *

# Core package imports
from .permit import Event
from .result import Result
from .color import GameColor
from .validator import Validator
from .mouse import MousePlacementStatus
from .emit import emitter

# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.common"

# Export control - only what belongs in public API
__all__ = [
    # Core classes
    "Event",
    "Result",
    "GameColor",
    "Validator",
    "MousePlacementStatus",
    "emit",

    *config,

    *exception.__all__,
    "exception",

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


