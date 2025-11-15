# src/chess/coord/__init__.py

"""
Module: chess.coord.__init__
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from .exception import *

from .dto import *
from .coord import Coord
from .builder import CoordBuilder
from .validator import CoordValidator

from .service import CoordService

# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.coord"


# Export control - only what belongs in public API
__all__ = [
    "CoordService",
    
    *exception.__all__,
    
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