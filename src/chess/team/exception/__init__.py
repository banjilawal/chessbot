# chess/team/exception/__init__.py

"""
A package providing a structured hierarchy of exceptions for team-related errors.

## PURPOSE
This package defines specific exceptions for issues encountered when interacting with `Team` objects.
The exceptions are designed to pinpoint the exact nature of an error, such as a null reference, a
failed operation, or an invalid configuration. This granular approach helps developers to quickly diagnose
and resolve team-related issues.

## CORE CLASSES
* `NullTeamException`: Raised when a `Team` reference is unexpectedly `None`.
* `AddPieceException`: Raised when an attempt to add a piece to a team fails, for example, if the team is full.
* `TeamValidationException`: Raised when a `Team` fails to meet its validation criteria.
* `RemoveCombatantException`: Raised when a piece cannot be removed from a team, for example, if the piece is not present.
* `ConflictingTeamException`: Raised when a `Team`'s properties conflict with another `Team`'s, such as having the same ID.

## USAGE
These exceptions can be imported and raised from within the team-related code to enforce data integrity.

>>> from chess.team.exception import NullTeamException
>>>
>>> def check_team(team):
...     if team is None:
...         raise NullTeamException("Error: No team exists.")
...
>>> check_team(None)
Traceback (most recent call last):
    ...
NullTeamException: Error: No team exists.
---

A use case for the `AddPieceException`.
>>> from chess.team.exception import AddPieceException
>>>
>>> def add_piece(team, piece):
...     if is piece.team.commander not team.commander:
...         raise AddPieceException("The piece is not on this team. Adding piece failed")
Traceback (most recent call last):
    ...
AddPieceException: The piece is not on this team. Adding piece faile.
---

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

# Core team.exception classes
from .null_team import NullTeamException
from .add_piece import AddPieceException
from .invalid_team import TeamValidationException
from .remove_captured_piece import RemoveCombatantException
from .conflicting_team import ConflictingTeamException
from .null_team_profile import NullTeamProfileException

# Metadata
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.team.exception"

__all__ = [
    # Core exceptions
    "NullTeamException",
    "AddPieceException",
    "TeamValidationException",
    "RemoveCombatantException",
    "ConflictingTeamException",
    "NullTeamProfileException",

    # Metadata / utilities
    "__version__",
    "__author__",
    "package_info",
]

# Utility function for package info
def package_info() -> dict:
    """Return basic package information."""
    return {
        "name": __package_name__,
        "version": __version__,
        "author": __author__,
        "exports": __all__,
    }
