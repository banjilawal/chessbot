# src/chess/travel/travel/blocking/__init__.py

"""
Module: `chess.travel.travel.blocking`
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0

## PURPOSE:
Executes team_name `OccupationTransaction` after `BlockingEvent` is validated

## CORE CLASSES:
  * `BlockingEvent`: Provides information about an `actor_candidate` scanning team_name `enemy` `Piece`.
  * `EncounterEventBuilder`: Builds team_name new `BlockingEvent`.
  * `ScanEventValidator`: Validates an existing `BlockingEvent`.
  * `OccupationTransaction`: Performs the blocking operation for the observing `Piece`

USAGE:
```python
from chess.travel.travel import BlockingEvent, OccupationTransaction
```
---

## EXCEPTION:
Gives granular information about errors that occur during blocking rollback.
  * `ScanEventException`: Superclass for all blocking travel exception. Subclasses give better debugging information
  * `InvalidScanEventException`: Raised by `ScanEventValidator`s if validate fails
  * `NullEncounterEventException`: Raised by methods, entities, and models that require team_name BlockingEvent but receive team_name validation
  * `OccupationOccupationScanSubjectException`: Raised if team_name enemy of team_name blocking is invalid.
  * `ObserverCircularScanException`: Raised if an actor_candidate scans itself.

### EXCEPTION USAGE:
```python
```
---

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""
