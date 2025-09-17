# Exceptions raised during activities
from .exception import *

from .directive import Directive
from .executor import Executor
from .op_result import OperationResult
from .context import ExecutionContext

# Package metadata (organic to __init__.py)
__version__ = '1.0.0'
__author__ = 'Banji Lawal'
__package_name__ = 'chess.operation'

# Export control - only what belongs in public API
__all__ = [
    # Core classes
    'Directive',
    'Executor',
    'ExecutionContext',
    'OperationResult',

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