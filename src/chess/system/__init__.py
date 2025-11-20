# src/chess/system/__init__.py

"""
Module: chess.system.__init__
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


from .dto import *
from .err import *
from .color import *
from .context import *
from .event import *
from .utils import *
from .result import *
from .config import *
from .search import *
from .build import *
from .logging import *
from .validate import *
from .identity import *
from .service import *
from .transaction import *


# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.system"

# Export control - only what belongs in public API
__all__ = [
  # Core classes


  # *color.__all__,
  # *dto.__all__,
  # *event.__all__,
  # *utils.__all__,
  # *result.__all__,
  # *search.__all__,
  # *build.__all__,
  # *identity.__all__,
  # *validate.__all__,
  # *err.__all__,
  # *logging.__all__,
  # *config.__all__,
  # *.service.__all__,
  # *transaction.__all__,

  # Package metadata and utilities
  "__version__",
  "__author__",
  "package_info",
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


