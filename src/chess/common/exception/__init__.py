from .conflict_exception import ResultPayloadConflictException

PayloadConflict = ResultPayloadConflictException


# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "common_exception_pkg"


# Organic utility function for package info
def package_info() -> dict:
    """Return basic package information."""
    return {
        "name": __package_name__,
        "version": __version__,
        "author": __author__,
        "exports": __all__
    }


# Export control - only what belongs in public API
__all__ = [
    # Core classes
    "ResultPayloadConflictException",
    "PayloadConflict",

    # Package metadata and utilities
    "__version__",
    "__author__",
    "package_info",
]