# src/chess/system/__init__.py

"""
Module: chess.system.__init__
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

#=========== SYSTEM PACKAGE CONTENTS ===========#

# Packages
from .build import *
from .color import *
from .config import *
from .context import *
from .data import *
from .dto import *
from .err import *
from .event import *
from .find import *
from .identity import *
from .logging import *
from .lookup import *
from .metadata import *
from .mouse import *
from .notification import *
from .result import *
from .resolution import *
from .service import *
from .text import *
from .transaction import *
from .utils import *
from .validate import *

# Modules
None



#
#
#
# # Package metadata (organic to __init__.py)
# __version__ = "1.0.0"
# __author__ = "Banji Lawal"
# __package_name__ = "chess.system"
#
# # Export control - only what belongs in public API
# __all__ = [
#   # Core classes
#     *build.__all__,
#     *color.__all__,
#     *config.__all__,
#     *map.__all__,
#     *dto.__all__,
#     *err.__all__,
#     *event.__all__,
#     *identity.__all__,
#     *logging.__all__,
#     *mouse.__all__,
#     *notification.__all__,
#     *result.__all__,
#     *searcher.__all__,
#     *entity_service.__all__,
#     *searcher.__all__,
#     *transaction.__all__,
#     *utils.__all__,
#     *validate.__all__,
#
#   # Package metadata and utilities
#   "__version__",
#   "__author__",
#   "package_info",
# ]
#
# # Organic utility function for package info
# def package_info() -> dict:
#   """Return basic package information."""
#   return {
#     "designation": __package_name__,
#     "version": __version__,
#     "author": __author__,
#     "exports": __all__
#   }
#
#
