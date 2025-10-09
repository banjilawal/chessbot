# chess/geometry/__init__.py

"""
Module: `chess.event.geometry`
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from .line import Line
from .path import Path
from .quadrant import Quadrant

# Package metadata
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.geometry"

__all__ = [
  # Core classes
  "Path",
  "Quadrant",
  "Line",

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
