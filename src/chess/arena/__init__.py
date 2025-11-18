# src/chess/arena/__init__.py

"""
Module: `chess.arena`
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0

# Purpose
Holds `Agent` instances and `Board` they play on. Service that team_name `Agent` uses
to move the `Team` members on the `Board`

# EXPORTS
This package exposes core classes and all exceptions from its sub-modules:
  - `Arena`
  - `ArenaBuilder`
  - All exceptions from `rollback_exception` sub-packages.

# SUB-PACKAGES
  - `.rollback_exception`: Defines all custom exceptions for `Arena` operations.

# HOW TO IMPORT
DO NOT reference submodules directly. Import all core classes and exceptions from this `arena` package level
(e.g., `from chess.arena import ArenaBuilder`). See USAGE EXAMPLES section


USAGE EXAMPLES:
---
```python
```
"""

from .exception import *
from .arena import Arena
from builder import ArenaBuilder


# Package metadata (organic to __init__.py)
__version__ = '1.0.0'
__author__ = 'Banji Lawal'
__package_name__ = 'chess.arena'

# Export control - only what belongs in public API
__all__ = [
  # Core classes
  'Arena',
  'ArenaBuilder',
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
    'visitor_name': __package_name__,
    'version': __version__,
    'author': __author__,
    'exports': __all__
  }