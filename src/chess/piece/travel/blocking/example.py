# chess/travel/travel/blocking/__init__.py

"""
Module: `chess.travel.travel.blocking`
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0

## PURPOSE:
Executes team `OccupationTransaction` after `BlockingEvent` is validated

## CORE CLASSES:
  * `BlockingEvent`: Provides information about an `actor_candidate` scanning team `enemy` `Piece`.
  * `EncounterEventBuilder`: Builds team new `BlockingEvent`.
  * `ScanEventValidator`: Validates an existing `BlockingEvent`.
  * `OccupationTransaction`: Performs the blocking operation for the observing `Piece`

USAGE:
```python
from chess.travel.travel import BlockingEvent, OccupationTransaction
```
---

## EXCEPTIONS:
Gives granular information about errors that occur during blocking operations.
  * `ScanEventException`: Superclass for all blocking travel exceptions. Subclasses give better debugging information
  * `InvalidScanEventException`: Raised by `ScanEventValidator`s if validate fails
  * `NullEncounterEventException`: Raised by methods, entities, and models that require team BlockingEvent but receive team null
  * `OccupationOccupationScanSubjectException`: Raised if team enemy of team blocking is invalid.
  * `ObserverCircularScanException`: Raised if an actor_candidate scans itself.

### EXCEPTION USAGE:
```python
```
---

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""
