# chess/vector/__init__py

"""
A package providing core classes for vector-based operations.

## PURPOSE
This package contains the foundational objects for vector arithmetic, handling transforms on
`Coord` objects. A `Vector` represents an offset that defines a path from a source to a
destination coordinate.

### CORE CLASSES
* `Vector`: An immutable class representing a two-dimensional offset.
* `VectorValidator`: Provides validation for `Vector` objects to ensure data integrity.

### USAGE
To use this package, import the desired classes and perform operations.

>>> from chess.vector import Vector, VectorValidator
>>>
>>> # Create and validate a vector instance
>>> candidate = Vector(x=2, y=1)
>>>
>>> # Validator.validate returns a Result
>>> validation = VectorValidator.validate(candidate)
>>> if not validation.is_success():
>>>     raise validation.team_exception
>>> # On success always cast the payload to its type.
>>> vector = cast(Vector, validation.payload)


## EXCEPTION CLASSES
This package defines a collection of specific exceptions for issues encountered when
working with `Vector` instances. The primary goal is to provide a clean and
consistent way to handle common vector-related errors, such as null values or
out-of-bounds components. This granular approach helps developers quickly
diagnose and resolve issues by pinpointing the exact nature of the problem.

### CORE EXCEPTIONS
* `NullVectorException`
* `XComponentNullException`
* `NullYComponentException`
* `VectorBelowBoundsException`
* `VectorAboveBoundsException`

## EXAMPLE EXCEPTION USAGE
These exceptions can be imported and raised within vector-related code to enforce
data integrity. They allow calling code to use specific `try...except` blocks
to handle different error conditions gracefully. For example:

# >>> from chess.vector.team_exception import XComponentNullException, VectorBelowBoundsException
>>> from chess.vector import Vector
>>>
>>> try:
...     # This will raise a VectorBelowBoundsException
...     vector = Vector(x=-100, y=3)
... except VectorBelowBoundsException as e:
...     print(f'Error: {e}')
...
>>> try:
...     # This will raise an XComponentNullException
...     vector = Vector(x=None, y=3)
... except NullXComponentException as e:
...     print(f'Error: {e}')

Classes, modules and functions that require a not-null `Vector` raise `NullVectorException`. A `Vector` cannot raise
`NullVectorException` on itself.

---
VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

from .exception import  *

# Core Vector classes
from .vector import Vector
from .vector_builder import VectorBuilder
from .vector_validator import VectorValidator


# Package metadata
__version__ = '1.0.0'
__author__ = 'Banji Lawal'
__package_name__ = 'chess.vector'

__all__ = [
    # Core classes
    'Vector',
    'VectorBuilder',
    'VectorValidator',

    *exception.__all__,


    # Package metadata and utilities
    '__version__',
    '__author__',
    'package_info'
]

# Organic utility function for package info
def package_info() -> dict:
    '''Return basic package information.'''
    return {
        'name': __package_name__,
        'version': __version__,
        'author': __author__,
        'exports': __all__
    }