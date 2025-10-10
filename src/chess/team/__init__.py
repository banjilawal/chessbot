# src/chess/team/__init__.py

"""
Module: chess.team
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""


from .schema import *
from .search import *
from .exception import *

from .team import Team
from .builder import TeamBuilder
from .validator import TeamValidator


# Metadata
__version__ = '1.0.0'
__author__ = 'Banji Lawal'
__package_name__ = 'chess.team'

# Optional: Package-level constants
ROSTER_SIZE = 16

# Public exports (API)
__all__ = [
  # Core classes
  'Team',
  'TeamValidator',
  'TeamBuilder',

  *roster_search.__all__,
  *schema.__all__,
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


