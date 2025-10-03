# src/chess/common/__init__.py

"""
Common Package - Objects used frequently and globally accross packages

## PURPOSE:
    Contains commonly used objects and utilites

## CORE CLASSES:
    Event, Result, GameColor, MousePlacementStatus


## USAGE EXAMPLES

## EXCEPTIONS

###


VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

from .id import *
from .name import *
from .actor import *
from .context import *
from .utils import *
from .result import *
from .config import *
from .emitter import *
from .validator import Validator


# Package metadata (organic to __init__.py)
__version__ = '1.0.0'
__author__ = 'Banji Lawal'
__package_name__ = 'chess.common'

# Export control - only what belongs in public API
__all__ = [
    # Core classes
    'ExecutionContext',
    'Validator',

    *id.__all__,
    *name.__all__,
    *utils.__all__,
    *actor.__all__,
    *result.__all__,
    *emitter.__all__,
    *config.__all__,

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


