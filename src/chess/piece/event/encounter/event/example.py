# chess/event/event/encounter/__init__.py

"""
Module: `chess.event.event.encounter`
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0

## PURPOSE:
Executes team `OccupationTransaction` after `EncounterEvent` is validated

## CORE CLASSES:
  * `EncounterEvent`: Provides information about an `actor_candidate` scanning team `enemy` `Piece`.
  * `EncounterEventBuilder`: Builds team new `EncounterEvent`.
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
  * `NullEncounterEventException`: Raised by methods, entities, and models that require team EncounterEvent but receive team null
  * `OccupationOccupationScanSubjectException`: Raised if team enemy of team encounter is invalid.
  * `ObserverCircularScanException`: Raised if an actor_candidate scans itself.

### EXCEPTION USAGE:
```python
```
---

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""
