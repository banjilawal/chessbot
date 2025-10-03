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

>>> from chess.scalar import Scalar, ScalarBuilder, ScalarValidator
>>> from typing import cast
>>> from chess.system import BuildResult
>>> from chess.vector import Vector
>>>
>>> # Create a scalar instance
>>> build_outcome = ScalarBuilder.build(value=1)
>>> if not build_outcome.is_success():
>>>     raise build_outcome.exception
>>> validation = ScalarValidator.validate(build_outcome.payload)
>>>
>>> # Validating the candidate
>>> if not validation.is_success():
>>>     raise validation.exception
>>> c = cast(Scalar, validation.payload)
>>>
>>> # Use the scalar to transform a vector
>>> u = Vector(x=3, y=4)
>>> v = u.scalar_product(c)
>>> print(v.x, v.y)
6, 8


## SCALAR EXCEPTONS
This package defines specific exceptions for issues encountered when working with scalar values. This granular approach helps developers to quickly diagnose and resolve problems such as a null scalar, or a value falling outside of a defined range.

## CORE EXCEPTIONS
* `NullScalarException`: Raised when a required scalar value is unexpectedly `None`.
* `ScalarBelowBoundsException`: Raised when a scalar's value is below its minimum allowed value.
* `ScalarAboveUpperBoundException`: Raised when a scalar's value is above its maximum allowed value.
* `InvalidScalarException`: A general team_exception raised when a scalar value fails to meet its validation criteria.

### EXCEPTION USAGE EXCEPTIONS
These exceptions can be imported and raised from within the scalar-related code to enforce data integrity.

>>> from chess.scalar import Scalar, NullScalarException, ScalarAboveBoundsException
>>>
>>> try:
...     # This will raise a NullScalarException
...     my_scalar = None
...     if my_scalar is None:
...         raise NullScalarException('Scalar cannot be null.')
... except NullScalarException as e:
...     print(f'Error: {e}')
...
>>> try:
...     # This will raise a ScalarAboveUpperBoundException
...
...     from chess.system import ROW_SIZE
...     my_scalar = Scalar(value=(ROW_SIZE + 1))
... except ScalarAboveBoundsException as e:
...     print(f'Error: {e}')

---
VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

# Include subpackages
from .exception import *

# Core  classes
from .scalar import Scalar
from .builder import ScalarBuilder
from .validator import ScalarValidator

# Package metadata
__version__ = '1.0.0'
__author__ = 'Banji Lawal'
__package_name__ = 'chess.scalar'

__all__ = [
    # Core classes
    'Scalar',
    'ScalarBuilder',
    'ScalarValidator',

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
