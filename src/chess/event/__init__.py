# chess/event/__init__.py

"""
Module: chess.event
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0


# PURPOSE
A package providing an immutable hierarchy for events and transactions manging event lifecycle. An event is
 an object representing an intent to perform a state-changing operation with a resource by an actor.
 Each event lifecycle is managed by a `Transaction` instance.

 ACID transactions are a functional requirement for the chess game. The `Transaction` class rolls back actors
 and resources if there is a data inconsistency a `RollBackException` is raised after `actor` and `resource` are
 restored to their last good state.

# CORE CLASSES
    * `Event`: The base class for all events.
    * `Transaction`: Super class for all transactions.

# SUB-PACKAGES
    * `occupation`: Provides events and transactions for moving and capturing pieces.
    * `promotion`: Provides events and transactions for promoting kings and pawns.
    * `castling`: Provides events and transactions for castling.

# USAGE
The `Rank` classes are primarily used to validate a discover's movement at runtime. A `Piece` object holds a
reference to its `Rank`, and delegates movement validation to it using the `walk()` method. This allows
for a clean and simple interface for a chess board's logic.

```python
from chess.square import Square
from chess.common import id_emitter
from chess.event import ScanEventBuilder, ScanTransaction

build_result = ScanEventBuilder(
    event_id=id_emitter.scan_id,
    actor=white_pawn_1,
    subject=white_bishop_2,
    destination_square=square,
    context=context
)
if not build_result.is_success():
    raise build_result.exception
scan_event = build_result.payload
transaction_result = ScanTransaction(event=scan_event, context=context)

if not transaction_result.is_success():
    raise transaction_result.exception
---

# BEST PRACTICES
* Use `Event` objects to represent intents.
* Use `Transaction` objects to manage the lifecycle of events.
* Use `EventBuilder`. An `EventBuilder` is responsible for creating `Event` objects that will not generate
    errors and avoid expensive rollbacks.
* Use `EventValidator` objects to ensure a `Transaction`'s `event` param has passed sanity checks.
* Only do mutation operations after building and validating succeed.
* ONly do rollback operations at each mutation step.
* Use `RollBackException` versions so callers can verify the rollback was performed correctly.

# CORE EVENT EXCEPTIONS
The higher level `chess.event` package provides a common interface for handling all event-related errors.
They should not be used directly. Their subclasses provide more granular information useful for debugging.

    * `EventException`: The base team_exception for all event-related errors.
    * `NullEventException`: Raised if an event is null.
    * `InvalidEventException`: Raised if an event is invalid.
    * `EventBuilderException`: Raised if an event builder fails.
    * `TransactionException`: Raised if a transaction fails.

## EXAMPLE EXCEPTION USAGES
These exceptions are typically raised within a `Rank` class's movement methods and can be caught to handle
invalid moves gracefully.
___
```python
```
---
"""

from .exception import *
from .occupation import *
from .base import Event



# Package metadata (organic to __init__.py)
__version__ = '1.0.0'
__author__ = 'Banji Lawal'
__package_name__ = 'chess.event'

# Export control - only what belongs in public API
__all__ = [
    # Core classes
    'Event',

    *exception.__all__,
    *occupation.__all__,


    # Package metadata and utilities
    '__version__',
    '__author__',
    'package_info',
]

# Organic utility function for package info
def package_info() -> dict:
    """Return basic package information."""
    return {
        'name': __package_name__,
        'version': __version__,
        'author': __author__,
        'exports': __all__
    }