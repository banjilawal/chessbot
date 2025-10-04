# chess/system/err/__init__.py

"""
Module: chess.system.err
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0

# PURPOSE
High level exceptions inherited by subclasses in the system. Utilities for centralizing
clean error handling and logging

 # EXPORTS
This package exposes core classes and all exceptions from its sub-modules:
    - `ChessException`: The base class exceptions in the application.
    - `NullException`: Super class for all null exceptions.
    - `ErrorHandler`: Logs the errors
    - `ErrorPropagator`: Coordinates re-raising and logging errors



# USAGE EXAMPLES
___
```python
```
---

# BEST PRACTICES
* Use a builder
"""

from .exception import *
from handler import ErrorHandler
from .propagator import ErrorPropagator


# Package metadata (organic to __init__.py)
__version__ = '1.0.0'
__author__ = 'Banji Lawal'
__package_name__ = 'chess.system.err'

# Export control - only what belongs in public API
__all__ = [
    # Core classes
    'ErrorHandler',
    'ErrorPropagator',

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