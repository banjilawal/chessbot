# src/chess/team/search/__init__.py

"""
Module: chess.team.search
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0


# PURPOSE
Search

# EXPORTS
This package exposes core classes and all exceptions from its sub-modules:
  - `CLASS>ANE`: <LINE_ABOUT_CLASS_PURPOSE_HERE>.
  - All exceptions from `exception` package.

# SUB-PACKAGES
  - `.exception`: Defines all custom exceptions for occupation operations.
  - `.ADDITIONAL_SUB_PACKAGE`: Logic for capturing, promoting, castling, and moving pieces on `Board`.

# HOW TO IMPORT
DO NOT reference submodules directly. Import all core classes and exceptions from this `board` package level
(e.g., `from chess.board import InvalidBoardException`). See USAGE EXAMPLES section

# USAGE EXAMPLES
___
```python
```
---
"""

from .exception import *
from .context import PieceSearchContext
from .builder import PieceSearchContextBuilder
from .validator import PieceSearchContextValidator

# Package metadata (organic to __init__.py)
__version__ = '1.0.0'
__author__ = 'Banji Lawal'
__package_name__ = 'chess.team.search.context'

# Export control - only what belongs in public API
__all__ = [
    'PieceSearchContext',
    'PieceSearchContextBuilder',
    'PieceSearchContextValidator',
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