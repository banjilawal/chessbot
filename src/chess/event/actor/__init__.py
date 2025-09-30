from .exception import *
from .builder import ActorBuilder
from .validator import ActorValidator


# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.event.actor"


# Export control - only what belongs in public API
__all__ = [
    # Core classes
    'ActorBuilder',
    'ActorValidator',

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