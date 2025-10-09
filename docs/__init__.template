# chess/vector/__init__.py

"""
Module: `chess.vector`
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from .exception import *

from .vector import Vector
from .builder import VectorBuilder
from .validator import VectorValidator

# Package metadata
__version__ = '1.0.0'
__author__ = 'Banji Lawal'
__package_name__ = 'chess.vector'

__all__ = [
  # Exported classes and utilities
  'Vector',
  'VectorBuilder',
  'VectorValidator',

  *exception.__all__,

  # Package metadata and utilities
  '__version__',
  '__author__',
  'package_info'
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