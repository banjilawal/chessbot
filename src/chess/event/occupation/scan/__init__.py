# src/chess/event/occupation/scan/__init__.py__init__.py

"""
# `chess.event.occupation.scan` Package

## PURPOSE:
Executes a `ScanTransaction` after `ScanEvent` is validated

## CORE CLASSES:
    * `ScanEvent`: Provides information about an `observer` scanning a `subject` `Piece`.
    * `ScanEventBuilder`: Builds a new `ScanEvent`.
    * `ScanEventValidator`: Validates an existing `ScanEvent`.
    * `ScanTransaction`: Performs the scan operation for the observing `Piece`

USAGE:
```python
from chess.event.occupation import ScanEvent, ScanTransaction
```
---

## EXCEPTIONS:
Gives granular information about errors that occur during scan operations.
    * `ScanEventException`: Superclass for all scan event exceptions. Subclasses give better debugging information
    * `InvalidScanEventException`: Raised by `ScanEventValidator`s if validation fails
    * `NullScanEventException`: Raised by methods, entities, and models that require a ScanEvent but receive a null
    * `InvalidScanSubjectException`: Raised if a subject of a scan is invalid.
    * `ObserverCircularScanException`: Raised if an observer scans itself.

### EXCEPTION USAGE:
```python
```
---

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

from .exception import *
from .event import ScanEvent
from .builder import ScanEventBuilder
from .validator import ScanEventValidator
from .transaction import ScanTransaction

# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.event.occupation.scan"


# Export control - only what belongs in public API
__all__ = [
    # Core classes
    'ScanEvent',
    'ScanEventBuilder',
    'ScanEventValidator',
    'ScanTransaction',

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