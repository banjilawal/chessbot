"""
Geometry Validatio Package - Validators for Geometry Packages

PURPOSE:
    Validating Geometry objects

CORE CLASSES:
    CoordValiadtor
    VectorValidator
    ScalarValidator

USAGE:
    >>> from chess.geometry.validator import VectorValidator
    >>> vector = Vector(x=-5, y=-3)
    >>> validation = VectorValidator.validate(vector)

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

# Core classes
from .coord_validator import CoordValidator
from .scalar_validator import ScalarValidator
from .vector_validator import VectorValidator


# Package metadata
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "geometry"


# Organic utility function for package info
def package_info() -> dict:
    """Return basic package information."""
    return {
        "name": __package_name__,
        "version": __version__,
        "author": __author__,
        "exports": __all__
    }


__all__ = [
    # Core classes

    # Subpackage



    # Package metadata and utilities
    "__version__",
    "__author__",
    "package_info"
]