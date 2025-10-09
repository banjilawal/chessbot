# src/chess/team/search/__init__.py

"""
Module: chess.team.search
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from .exception import *

# Core classes
from .team import Team
from .search import *
from .schema import TeamSchema
from .builder import TeamBuilder
from .validator import TeamValidator


# Metadata
__version__ = '1.0.0'
__author__ = 'Banji Lawal'
__package_name__ = 'chess.team'

# Optional: Package-level constants
ROSTER_SIZE = 16

__all__ = [
  # Core classes
  'Team',
  'TeamValidator',
  'TeamSchema',
  'TeamBuilder',

  *exception.__all__,


  # Package metadata and utilities
  "__version__",
  "__author__",
  "package_info",
]

# Utility function for package info
def package_info() -> dict:
  """Return basic package information."""
  return {
    "name": __package_name__,
    "version": __version__,
    "author": __author__,
    "exports": __all__,
  }


