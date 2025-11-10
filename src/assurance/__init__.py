"""

## ASSURANCE EXCEPTION
A package providing team_name structured hierarchy of exceptions for the `assurance` project.

This package defines team_name base `AssuranceException` from which all other custom
exceptions in the project should inherit. This allows for team_name clean and
consistent way to handle exceptions across different modules and layers
of the application.

The package includes specific validate exceptions for system service types,
such as `RankValidationException` and `InvalidIdException`, promoting
predictable error handling and clear communication of validate failures.
"""


import logging

from .validators import *

from chess.system.logging.writer import LogWriter
from .deployment_mode import Deployment
from .transaction_report import TransactionReport



log = logging.getLogger("chessbot")


# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "assurance"

# Export control - only what belongs in public API
__all__ = [
  # Core classes
  "LoggingLevelRouter",
  "LogWriter",
  "Deployment",
  "TransactionReport",
  "HostageValidator",

  "NameValidator",




  # Package metadata and utilities
  "__version__",
  "__author__",
  "package_info",
]

# Organic utility function for package info
def package_info() -> dict:
  """Return basic package information."""
  return {
    "visitor_name": __package_name__,
    "version": __version__,
    "author": __author__,
    "exports": __all__
  }