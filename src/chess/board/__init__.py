# src/chess/board/__init__.py

"""
# `chess.board` Package

## PURPOSE:
    Board related classes

## CORE CLASSES
    * `Board`:
    * `SquareIterator`:

### USAGE EXAMPLES
    These examples show recommended workflows with `chess.board` classes.

```python
from chess.board import Board, SquareIterator
```
___

## EXCEPTIONS
raised by chess.board classes are defined in the chess.board.exception subpackage.

### EXCEPTION USAGE EXAMPLES
These examples show recommended workflows with `chess.board` exceptions.
---
```python
```
___
#

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

# Subpackage imports
from .exception import *

# Core class
from .exception import *
from .board import Board
from .search import BoardSearch
from .square_iterator import SquareIterator

# Package metadata (organic to __init__.py)
__version__ = '1.0.0'
__author__ = 'Banji Lawal'
__package_name__ = 'chess.board'

# Export control - only what belongs in public API
__all__ = [
    # Core classes
    'Board',
    'BoardSearch',
    'SquareIterator',

    *exception.__all__,

    # Package metadata and utilities
    '__version__',
    '__author__',
    'package_info',
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

