# chess/scalar/exception/__init__.py

"""
A package providing a structured hierarchy of exceptions for scalar values.

## PURPOSE
This package defines specific exceptions for issues encountered when working with scalar values. This granular approach helps developers to quickly diagnose and resolve problems such as a null scalar, or a value falling outside of a defined range.

## CORE CLASSES
* `NullScalarException`: Raised when a required scalar value is unexpectedly `None`.
* `ScalarBelowBoundsException`: Raised when a scalar's value is below its minimum allowed value.
* `ScalarAboveUpperBoundException`: Raised when a scalar's value is above its maximum allowed value.
* `ScalarValidationException`: A general exception raised when a scalar value fails to meet its validation criteria.

## USAGE
These exceptions can be imported and raised from within the scalar-related code to enforce data integrity.

>>> from chess.scalar.exception import NullScalarException, ScalarAboveBoundsException
>>> from chess.scalar import Scalar
>>>
>>> try:
...     # This will raise a NullScalarException
...     my_scalar = None
...     if my_scalar is None:
...         raise NullScalarException("Scalar cannot be null.")
... except NullScalarException as e:
...     print(f"Error: {e}")
...
>>> try:
...     # This will raise a ScalarAboveUpperBoundException
...
...     from chess.common import ROW_SIZE
...     my_scalar = Scalar(value=(ROW_SIZE + 1))
... except ScalarAboveBoundsException as e:
...     print(f"Error: {e}")

---
VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

from .null_scalar import NullScalarException
from .below_bounds import ScalarBelowBoundsException
from .above_bounds import ScalarAboveBoundsException
from .invalid_scalar import ScalarValidationException

# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.scalar.exception"

__all__ = [
    # Core classes
    "NullScalarException",
    "ScalarBelowBoundsException",
    "ScalarAboveBoundsException",
    "ScalarValidationException",

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