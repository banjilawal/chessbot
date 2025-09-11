# chess/vector/exception/__init__py

"""
A package providing a structured hierarchy of exceptions for vector objects.

## PURPOSE
This package defines a collection of specific exceptions for issues encountered when
working with `Vector` instances. The primary goal is to provide a clean and
consistent way to handle common vector-related errors, such as null values or
out-of-bounds components. This granular approach helps developers quickly
diagnose and resolve issues by pinpointing the exact nature of the problem.

## CORE CLASSES
* `NullVectorException`
* `XComponentNullException`
* `YComponentNullException`
* `VectorBelowBoundsException`
* `VectorAboveBoundsException`

## USAGE
These exceptions can be imported and raised within vector-related code to enforce
data integrity. They allow calling code to use specific `try...except` blocks
to handle different error conditions gracefully. For example:

>>> from chess.vector.exception import XComponentNullException, VectorBelowBoundsException
>>> from chess.vector import Vector
>>>
>>> try:
...     # This will raise a VectorBelowBoundsException
...     vector = Vector(x=-100, y=3)
... except VectorBelowBoundsException as e:
...     print(f"Error: {e}")
...
>>> try:
...     # This will raise an XComponentNullException
...     vector = Vector(x=None, y=3)
... except XComponentNullException as e:
...     print(f"Error: {e}")

Classes, modules and functions that require a not-null `Vector` raise `NullVectorException`. A `Vector` cannot raise
`NullVectorException` on itself.

>>> from chess.vector.exception import NullVectorException
>>> from chess.vector import Vector
>>> from chess.coord import Coord
>>>
>>> try:
...     origin = Coord(row=2, column=0)
...     vector = None
...     if vector is None:
...         raise NullVectorException(f"{NullVectorException.DEFAULT_MESSAGE}")
...     destination = origin.add_vector(vector)
... except NullVectorException as e:
...     print(f"Error: {e}")

---
VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

from .null_vector import NullVectorException
from .null_x import XComponentNullException
from .null_y import YComponentNullException

from .below_bounds import VectorBelowBoundsException
from .above_bounds import VectorAboveBoundsException

# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.vector.exception"

__all__ = [
    # Core Packages
    "NullVectorException",
    "XComponentNullException",
    "YComponentNullException",

    "VectorBelowBoundsException",
    "VectorAboveBoundsException",

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