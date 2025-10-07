# chess/system/search/__init__.py

"""
Module: chess.system.search
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0

# PURPOSE
Super class for `Search` objects and their components.

 # EXPORTS
  - `Search`: The base class for `Search` objects.
  - `SearchResult`: Data class returned by `Search` instances
  - `SearchContext`: Abstract super class for `SearchContext` objects.
  - All exceptions in the `exception` subpackage

# SUB-PACKAGES
  - `.exception`: Defines all custom exceptions for event operations.


# USAGE EXAMPLES
___
```python
```
---
"""

from .exception import *
from .context import *


# Package metadata (organic to __init__.py)
__version__ = '1.0.0'
__author__ = 'Banji Lawal'
__package_name__ = 'chess.system.search.context'

# Export control - only what belongs in public API
__all__ = [

  *context.__all__,
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
    'exports':__all__
  }