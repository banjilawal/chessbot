# src/chess/coord/__init__.py

"""
# `chess.coord` Package

## Purpose
Provides immutable `(row, column)` coordinate tuples for board positions, with builders and validators for safe
creation and validation.

## Core Classes
    - `Coord`: Immutable `(row, column)` coordinate object.
    - `CoordBuilder`: Safely constructs validated `Coord` instances.
    - `CoordValidator`: Validates existing `Coord` instances.

## Usage
```python
from typing import cast
from chess.coord import Coord, CoordBuilder

build_outcome = CoordBuilder.build(row=0, column=7)
if not build_outcome.is_success():
    raise build_outcome.exception

# Always cast the payload to the desired type before using it
coord = cast(Coord, build_outcome.payload)
print(coord)
```

## COORD EXCEPTIONS
These are not all the exceptions related to `Coord` in the application. `chess.coord` package only has exceptions
organic to:
    * `Coord`
    * `CoordBuilder`
    * `CoordValidator`

All exceptions in `chess.coord` package have static fields:
    - `ERROR_CODE`: Useful when parsing logs for an exception. Error codes are in caps with a "_ERROR" suffix
    - `DFAULT_MESSAGE`: A sentence describing the exception. Use an exception's `DEFAULT_MESSAGE`
For consistency across the application.

### LIST OF EXCEPTIONS:
    * `CoordException`: Superclass for Coord-related exceptions
    * `NullCoordException`: Raised if a coordinate is null
    * `CoordValidationException`: Raised if coordinate validation fails
    * `NullCoordValidatorException`: Raised if a CoordValidator is null
    * `CoordBuilderException`: Wrapper for exceptions raised by CoordBuilder
    * `NullCoordBuilderException`: Raised if a CoordBuilder is null
    * `NullRowException`: Raised if a row is null (Coord cannot be created)
    * `RowBelowBoundsException`: Raised if row < 0
    * `RowAboveBoundsException`: Raised if row >= ROW_SIZE
    * `NullColumnException`: Raised if a column is null (Coord cannot be created)
    * `ColumnBelowBoundsException`: Raised if column < 0
    * `ColumnAboveBoundsException`: Raised if column >= COLUMN_SIZE

### COORD EXCEPTION USAGE EXAMPLES
These examples show recommended workflows with `Coord` exceptions.
```python
from chess.coord import CombatantCoord, CoordBuilder
from chess.coord import Coord, NullCoordException, NullRowException

build_outcome = CoordBuilder.build(1, "BK", King(), black_team)
if not build_outcome.is_success():
    raise build_outcome.exception
coord = cast(KingCoord, build_outcome.payload)

coord = None
if coord is None:
    raise NullCoordException(NullCoordException.DEFAULT_MESSAGE)
coord.positions.push_coord(coord)
```

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

from .exception import *

from .coord import Coord
from .builder import CoordBuilder
from .validator import CoordValidator


# Package metadata
__version__ = '1.0.0'
__author__ = 'Banji Lawal'
__package_name__ = 'chess.coord'

__all__ = [
    # Core classes
    'Coord',
    'CoordException',
    'CoordValidator',

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