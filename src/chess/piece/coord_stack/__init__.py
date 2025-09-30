# chess/piece/coord_stack/__init__.py

"""
# `chess.piece.coord_stack` Package

## Purpose
Provides the data structures and utilities for storing history of `Piece` object's positions.

## Classes
    * `CoordStack`: Coordinate history and management utility. Only the last `Coord` can be removed in a turn.
    * `CoordStackValidator`: Integrity checks for an existing `CoordStack`.


## Usage
```python

```

## EXCEPTIONS
    * `CoordStackException`: Super class of exceptions raised by `CoordStack`.
    * `DoubleCoordPushException`: Raised when a `Coord` at the top of the stack is pushed again.
    * `CoordStackValidationException`: Raised if an existing `CoordStack` object fails validation.
    * `NullCoordStackException`: Raised if a null `CoordStackException` is passed as a parameter.

### EXCEPTION USAGE EXAMPLES
These examples show recommended workflows with `CoordStack` exceptions.

```python
from chess.piece import CoordStack, NullCoordStackException, CoordStackValidationException
```

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

from .exception import *
from .coord_stack import CoordStack
from .validator import CoordStackValidator


# Package metadata (organic to __init__.py)
__version__ = '1.0.0'
__author__ = 'Banji Lawal'
__package_name__ = 'chess.piece.coord_stack'


# Export control - only what belongs in public API
__all__ = [
    # Core classes
    'CoordStack',
    'CoordStackValidator',

    *exception.__all__,



    # Package metadata and utilities
    '__version__',
    '__author__',
    'package_info'
]

# Organic utility function for package info
def package_info() -> dict:
    """Return basic package information."""
    return {
        'name': __package_name__,
        'version': __version__,
        'author': __author__,
        'exports': __all__
    }
