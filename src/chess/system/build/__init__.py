# chess/system/build/__init__.py

"""
Module: chess.system.build
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0


# PURPOSE
The preferred way to build objects in the system. A `Builder` centralizes all the safety checks leaving constructors
clean.

 ACID transactions are a functional requirement for the chess game. The `Transaction` class rolls back actors
 and resources if there is a data inconsistency a `RollBackException` is raised after `actor` and `resource` are
 restored to their last good state.

 # EXPORTS
This package exposes core classes and all exceptions from its sub-modules:
  - `Builder`: The base class for `Build` objects.
  - All exceptions from `exception` package.

# SUB-PACKAGES
  - `.exception`: Defines all custom exceptions for occupation operations.
  - `.occupation`: Logic for capturing, promoting, castling, and moving pieces on `Board`.


# USAGE EXAMPLES
___
```python
```
---

# BEST PRACTICES
* Use a builder
"""

from .exception import *
from .builder import Builder
from .result import BuildResult


# Package metadata (organic to __init__.py)
__version__ = '1.0.0'
__author__ = 'Banji Lawal'
__package_name__ = 'chess.system.build'

# Export control - only what belongs in public API
__all__ = [
  # Core classes
  'Builder',
  'BuildResult',
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