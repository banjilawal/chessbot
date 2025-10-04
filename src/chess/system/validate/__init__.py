# chess/system/validate/__init__.py

"""
Module: chess.system.validate
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0

# PURPOSE
Validation super class and exceptions.


 # EXPORTS
    - `Validator`: The base class for `validate` objects.
    - `ValidationException`: The base class for `validate` exceptions.

# SUB-PACKAGES
    - `.exception`: Defines all custom exceptions for occupation operations.


# USAGE EXAMPLES
___
```python
```
---

# BEST PRACTICES
* Do not use `ValidationException` directly use the appropriate `ValidationException` subclass.
"""

from .exception import *
from .validator import Validator
from .result import ValidationResult



# Package metadata (organic to __init__.py)
__version__ = '1.0.0'
__author__ = 'Banji Lawal'
__package_name__ = 'chess.system.validate'

# Export control - only what belongs in public API
__all__ = [
    # Core classes
    'Validator',
    'ValidationResult',
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