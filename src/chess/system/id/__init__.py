# src/chess/system/__init__.py
"""
## PURPOSE:
    Id validation

## CORE CLASSES:
* `IdValidator`
* `IdNullException`
* `NegativeIdException`
* `InvalidIdException`


USAGE:
    >>>
    >>>

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

from .exception import *
from .validator import IdValidator


# Package metadata (organic to __init__.py)
__version__ = '1.0.0'
__author__ = 'Banji Lawal'
__package_name__ = 'chess.system.id'

# Export control - only what belongs in public API
__all__ = [
    # Core classes
    'IdValidator',

    *exception.__all__,

    # Package metadata and utilities
    '__version__',
    '__author__',
    'package_info',
]

# Organic utility function for package info
def package_info() -> dict:
    '''Return basic package information.'''
    return {
        'name': __package_name__,
        'version': __version__,
        'author': __author__,
        'exports': __all__
    }