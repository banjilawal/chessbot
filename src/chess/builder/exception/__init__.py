"""
chess.builder.exception Package

PURPOSE:
    Exceptions raised by Builder classes

CORE CLASSES:
    CommanderBuilderException
    CoordBuilderException
    PieceBuilderException
    ScalarBuilderException
    VectorBuilderException



USAGE:
    >>>
    >>>

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

# Subpackage imports

# Core imports
from .commander_builder_exception import CommanderBuilderException
from .coord_builder_exception import CoordBuilderException
from .piece_builder_exception import PieceBuilderException
from .scalar_builder_exception import ScalarBuilderException
from .vector_builder_exception import VectorBuilderException


# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.builder.exception"

# Export control - only what belongs in public API
__all__ = [
    # Core classes
    "CommanderBuilderException",
    "CoordBuilderException",
    "PieceBuilderException",
    "ScalarBuilderException",
    "VectorBuilderException",

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