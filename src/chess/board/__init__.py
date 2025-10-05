# chess/board/__init__.py

"""
Module: chess.board
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0

# Purpose
Provides board for game play. The package keeps track of pieces and provides addressing for `Square` objects
which a `Piece` instance can reside.

# EXPORTS
This package exposes core classes and all exceptions from its sub-modules:
  - `Board`:
  - `BoardBuilder`:
  - `BoarSearch`:
  - `SquareIterator`:
  - All exceptions from `exception` sub-packages.

# SUB-PACKAGES
  - `.exception`: Defines all custom exceptions for `Board` operations.

# HOW TO IMPORT
DO NOT reference submodules directly. Import all core classes and exceptions from this `board` package level
(e.g., `from chess.board import InvalidBoardException`). See USAGE EXAMPLES section

USAGE EXAMPLES:
---
```python
```
"""

from .board import Board
from .search import BoardSearch
from .square_iterator import SquareIterator

# Subpackage imports

# Module Imports
from .exception import *

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