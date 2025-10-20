# chess/event/event/attack__init__.py

"""
Module: `chess.event.event.attack`
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.piece.event.attack.event.exception import *
from chess.piece.event.attack.event.builder import AttackEventBuilder

# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.event.event.attack"


# Export control - only what belongs in public API
__all__ = [
  # Core classes
  'AttackEvent',
  'AttackEventBuilder',
  'AttackEventValidator',

  # Exception classes
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