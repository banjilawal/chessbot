# chess/square/__init__.py

"""
Module: `chess.square`
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from .exception import *
from .square import Square
from .builder import SquareBuilder
from .validator import SquareValidator

__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.square"

__all__ = [
  # Core Packages
  "Square",
  'SquareBuilder',
  "SquareValidator",

  *exception.__all__,

  # Package metadata and utilities
  "__version__",
  "__author__",
  "package_info"
]

# Organic utility function for package info
def package_info() -> dict:
  """Return basic package information."""
  return {
    "name": __package_name__,
    "version": __version__,
    "author": __author__,
    "exports": __all__
  }



