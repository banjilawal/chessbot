# chess/system/validation/__init__.py

"""
Module: chess.system.build
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0


# PURPOSE
Validation super clas and exceptions.


 # EXPORTS
This package exposes core classes and all exceptions from its sub-modules:
    - `Validator`: The base class for `validation` objects.
    - All exceptions from `exception` package.

# SUB-PACKAGES
    - `.exception`: Defines all custom exceptions for occupation operations.


# USAGE EXAMPLES
___
```python
```
---

# BEST PRACTICES
* Use `Event` objects to represent intents.
* Use `Transaction` objects to manage the lifecycle of events.
* Use `EventBuilder`. An `EventBuilder` is responsible for creating `Event` objects that will not generate
"""

from .exception import *
from .validator import Validator


# Package metadata (organic to __init__.py)
__version__ = '1.0.0'
__author__ = 'Banji Lawal'
__package_name__ = 'chess.system.validation'

# Export control - only what belongs in public API
__all__ = [
    # Core classes
    'Validator',
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