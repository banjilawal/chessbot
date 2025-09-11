# chess/vector/exception/__init__py

"""
A package providing core classes for vector-based operations.

## PURPOSE
This package contains the foundational objects for vector arithmetic, handling transforms on
`Coord` objects. A `Vector` represents an offset that defines a path from a source to a
destination coordinate.

## CORE CLASSES
* `Vector`: An immutable class representing a two-dimensional offset.
* `VectorValidator`: Provides validation for `Vector` objects to ensure data integrity.

## USAGE
To use this package, import the desired classes and perform operations.

>>> from chess.vector import Vector, VectorValidator
>>>
>>> # Create and validate a vector instance
>>> candidate = Vector(x=2, y=1)
>>>
>>> # Validator.validate returns a Result
>>> validation = VectorValidator.validate(candidate)
>>> if not validation.is_success():
>>>     raise validation.exception
>>> # On success always cast the payload to its type.
>>> vector = cast(Vector, validation.payload)

---
VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

# Include subpackages
from .exception import *

# Core Vector classes
from .vector import Vector
from .vector_validator import VectorValidator

# Package metadata
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.vector"

__all__ = [
    # Core classes
    "Vector",
    "VectorValidator",

    *exception.__all__,
    # Subpackage
    "exception",

    # Package metadata and utilities
    "__version__",
    "__author__",
    "package_info"
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