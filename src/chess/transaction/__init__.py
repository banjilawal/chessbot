# Exceptions raised during activities
from .exception import *
from chess.system.context import *

from chess.event.event import Event
from chess.event.transaction import Transaction
from chess.system.result.transaction import TransactionResult
from .attack_validator import AttackValidator


# Package metadata (organic to __init__.py)
__version__ = '1.0.0'
__author__ = 'Banji Lawal'
__package_name__ = 'chess.transaction'

# Export control - only what belongs in public API
__all__ = [
  # Core classes
  'Event',
  'Transaction',
  'ExecutionContext',
  'TransactionResult',
  'AttackValidator',


  *context.__all__,
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