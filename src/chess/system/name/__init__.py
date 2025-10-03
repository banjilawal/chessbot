# src/chess/system/__init__.py
"""
## PURPOSE:
    Name validation 

## CORE CLASSES:
* `NameValidator`
* `NameNullException`
* `NegativeNameException`
* `NameValnameationException`
* `NullNameException`
* `LongNameException`
* `ShortNameException`
* `BlankNameException`
* `NameValidationException`

USAGE:
    >>>
    >>>

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""


from .exception import *
from .validator import NameValidator


# Package metadata (organic to __init__.py)
__version__ = '1.0.0'
__author__ = 'Banji Lawal'
__package_name__ = 'chess.system.name'

# Export control - only what belongs in public API
__all__ = [
    # Core classes
    'NameValidator',

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