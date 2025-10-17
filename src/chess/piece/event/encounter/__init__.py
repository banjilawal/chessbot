# chess/event/event/encounter/__init__.py

"""
Module: `chess.event.event.encounter`
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0

## PURPOSE:
Executes team `OccupationTransaction` after `EncounterEvent` is validated

## CORE CLASSES:
  * `EncounterEvent`: Provides information about an `actor` scanning team `enemy` `Piece`.
  * `ScanEventBuilder`: Builds team new `EncounterEvent`.
  * `ScanEventValidator`: Validates an existing `EncounterEvent`.
  * `OccupationTransaction`: Performs the encounter operation for the observing `Piece`

USAGE:
```python
from chess.event.event import EncounterEvent, OccupationTransaction
```
---

## EXCEPTIONS:
Gives granular information about errors that occur during encounter operations.
  * `ScanEventException`: Superclass for all encounter event exceptions. Subclasses give better debugging information
  * `InvalidScanEventException`: Raised by `ScanEventValidator`s if validate fails
  * `NullScanEventException`: Raised by methods, entities, and models that require team EncounterEvent but receive team null
  * `OccupationOccupationScanSubjectException`: Raised if team enemy of team encounter is invalid.
  * `ObserverCircularScanException`: Raised if an actor scans itself.

### EXCEPTION USAGE:
```python
```
---

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

from .exception import *
from .event import EncounterEvent
from .builder import ScanEventBuilder
from .transaction import LogEncounterTransaction

# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.event.event.encounter"


# Export control - only what belongs in public API
__all__ = [
  # Core classes
  'EncounterEvent',
  'ScanEventBuilder',
  'ScanEventValidator',
  'LogEncounterTransaction',

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