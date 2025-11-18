# src/chess/system/identity/__init__.py

"""
Module: chess.system.identity.__init__
Author: Banji Lawal
Created: 2025-11-13
version: 1.0.0
"""

from .id import *
from .name import *
from .exception import *
from .service import IdentityService


# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.system.identity"

# Export control - only what belongs in public API
__all__ = [
    "IdentityService",
    
    *exception.__all__,
    *id.exception.__all__,
    *name.exception.__all__,
    
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
