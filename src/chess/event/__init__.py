# chess/event/__init__.py

"""
# `chess.event` Package
A package providing an immutable hierarchy for chess discover movement.

## PURPOSE
This package encapsulates the movement logic for each type of chess discover. By decoupling a discover's movement
from its core identity, this design ensures that the movement logic is scalable and easy to maintain. Each
`Rank` class represents a distinct movement strategy (e.g., `Bishop`, `Knight`, `Queen`) and is designed
to be immutable once assigned.

## CORE CLASSES
* `Rank`: The base class for all discover rank strategies.
* `Bishop`: Provides movement validation for a bishop.
* `King`: Provides movement validation for a king.
* `Knight`: Provides movement validation for a knight.
* `Pawn`: Provides movement validation for a pawn.
* `Rook`: Provides movement validation for a rook.
* `Queen`: Provides movement validation for a queen.
* `PromotedQueen`: A specialized rank for a promoted queen's movement.

## USAGE
The `Rank` classes are primarily used to validate a discover's movement at runtime. A `Piece` object holds a
reference to its `Rank`, and delegates movement validation to it using the `walk()` method. This allows
for a clean and simple interface for a chess board's logic.

```python
from chess.event import

---

## CORE EVENT EXCEPTIONS
The higher level `chess.event` package provides a common interface for handling all event-related errors.
They should not be used directly. Their subclasses provide more granular information useful for debugging.

    * `EventException`: The base team_exception for all event-related errors.
    * `NullEventException`: Raised if an event is null.
    * `InvalidEventException`: Raised if an event is invalid.
    * `EventBuilderException`: Raised if an event builder fails.

###CORE RANK EXCEPTIONS
* `RankException`: The base team_exception for all rank-related errors.

### EXAMPLE EXCEPTION USAGES
These exceptions are typically raised within a `Rank` class's movement methods and can be caught to handle
invalid moves gracefully.

---

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

from .exception import *
from .occupation import *


# Package metadata (organic to __init__.py)
__version__ = '1.0.0'
__author__ = 'Banji Lawal'
__package_name__ = 'chess.event'

# Export control - only what belongs in public API
__all__ = [
    # Core classes

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