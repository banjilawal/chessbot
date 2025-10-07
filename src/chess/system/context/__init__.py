# chess/system/roster/__init__.py

"""
Module: chess.system.roster
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0

# PURPOSE
Parent class of `Context` entities.

 # EXPORTS
This package exposes core classes and all exceptions from its sub-modules:
  - `Context`: The base class for `Context` objects.
  - All exceptions from `exception` package.

# SUB-PACKAGES
  - `.exception`: Defines all custom exceptions for event operations.

# USAGE EXAMPLES
___
```python
```
---

# BEST PRACTICES
* Use a builder
"""

from .exception import *
from .context import Context


# Package metadata (organic to __init__.py)
__version__ = '1.0.0'
__author__ = 'Banji Lawal'
__package_name__ = 'chess.system.roster'

# Export control - only what belongs in public API
__all__ = [
  # Core classes
  'Context',
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