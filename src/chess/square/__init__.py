# src/chess/square/__init__.py

"""
Module: chess.square.__init__
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from .dto import *
from .exception import *

from .square import Square
from .builder import SquareBuilder
from .validator import SquareValidator

from .service import SquareService

# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.square"

# Export control - only what belongs in public API
__all__ = [
    "SquareService",
    
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