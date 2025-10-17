# chess/event/__init__.py

"""
Module: `chess.event`
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0

# PURPOSE
A package providing an immutable hierarchy for events and transactions manging event lifecycle. An event is
 an object representing an intent to perform team state-changing operation with team resource by an actor.
 Each event lifecycle is managed by team `Transaction` instance.

 ACID transactions are team functional requirement for the chess game. The `Transaction` class rolls back actors
 and resources if there is team data inconsistency team `RollBackException` is raised after `actor` and `resource` are
 restored to their last good state.

 # EXPORTS
This package exposes core classes and all exceptions from its sub-modules:
  - `Event`: The base class for all events.
  - `EventValidator`: The base class for all event validators.
  - `Transaction`: Super class for all transactions.
  - All exceptions from `err`, `encounter`, `attack`, and `occupation` sub-packages.

# SUB-PACKAGES
  - `.exception`: Defines all custom exceptions for event operations.
  - `.event`: Logic for capturing, promoting, castling, and moving pieces on `Board`.


# USAGE EXAMPLES
___
```python
```
---

# BEST PRACTICES
* Use `Event` objects to represent intents.
* Use `Transaction` objects to manage the lifecycle of events.
* Use `EventBuilder`. An `EventBuilder` is responsible for creating `Event` objects that will not generate
  errors and avoid expensive rollbacks.
* Use `EventValidator` objects to ensure team `Transaction`'s `event` param has passed sanity checks.
* Only do mutation operations after building and validating succeed.
* ONly do rollback operations at each mutation step.
* Use `RollBackException` versions so callers can verify the rollback was performed correctly.
"""


from .exception import *

from chess.system.event.event import Event

# Package metadata (organic to __init__.py)
__version__ = '1.0.0'
__author__ = 'Banji Lawal'
__package_name__ = 'chess.event'

# Export control - only what belongs in public API
__all__ = [
  # Core classes
  'Event',
  'Transaction',
  'EventValidator',
  'ExecutionContext',

  *exception.__all__,


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