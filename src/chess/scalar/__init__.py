# chess/scalar/__init__.py

"""
A package providing core classes and utilities for scalar values.

## PURPOSE
This package contains the foundational objects for representing and validating scalar values. These values
 are used to multiply `Vector` and `Coord` objects, causing them to scale (grow or shrink) within their
 planes. This is a core component for scaling transformations.

## CORE CLASSES
* `Scalar`: A class representing a single numeric value used for scaling operations.
* `ScalarValidator`: A class that validates the data and integrity of a `Scalar` object.

## USAGE
To use this package, import the desired classes and perform scalar-related operations.

>>> from chess.scalar import Scalar, ScalarValidator
>>> from chess.vector import Vector
>>>
>>> # Create a scalar instance
>>> scalar = None
>>> candidate = Scalar(value=2)
>>> validation = ScalarValidator.validate(candidate)
>>>
>>> # Validating the candidate
>>> if not validation.is_success():
>>>     raise validation.exception
>>> scalar = cast(Scalar, validation.payload)
>>>
>>> # Use the scalar to transform a vector
>>> u = Vector(x=3, y=4)
>>> v = u.scalar_product(scalar)
>>> print(v.x, v.y)
6, 8

---
VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

# Include subpackages
from .exception import *

# Core  classes
from .scalar import Scalar
from .scalar_validator import ScalarValidator

# Package metadata
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.scalar"

__all__ = [
    # Core classes
    "Scalar",
    "ScalarValidator",

    # Subpackage
    *exception.__all__,
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
