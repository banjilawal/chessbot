# chess/scalar/__init__.py

"""
Module: chess.scalar.__init__
Author: Banji Lawal
Created: 2025-09-11
version: 1.0.0
"""


from .exception import *

from .scalar import Scalar
from .builder import ScalarBuilder
from .validator import ScalarValidator

from .service import ScalarService

# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.scalar"


# Export control - only what belongs in public API
__all__ = [
    "ScalarService",
    
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
        "visitor_name": __package_name__,
        "version": __version__,
        "author": __author__,
        "exports": __all__
    }