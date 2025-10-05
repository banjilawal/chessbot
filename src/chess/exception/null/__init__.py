
from .number_null_exception import NullNumberException
from .string_null_exception import NullStringException


# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.team_exception.null"

__all__ = [
  # Core classes
  "NullNumberException",
  "NullStringException",

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