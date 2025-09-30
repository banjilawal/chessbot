# chess/team/__init__py

"""
A package providing core classes and utilities for managing chess teams.

## PURPOSE
This package contains the foundational objects and logic for representing and managing chess teams. It defines the structure of a `Team`, maintains a roster of its `Piece` objects, and includes validation to ensure a correct configuration.

## CORE CLASSES
* `Team`: A class representing a chess team.
* `TeamProfile`: A class that stores descriptive information for a team, such as its name and ID.
        Neccessary for constructing a team
* `TeamValidator`: A class that provides validation and sanity checks for a team's configuration.

## USAGE
To use this package, import the desired classes and perform team-related operations.

>>> from chess.team import Team, TeamSchema, TeamValidator
>>> # Create a new team and roster
>>> team = Team(team_id=1, commander=white_team_commander, schema=TeamSchema.WHITE)
>>> validation = TeamValidator.validate(team)

## TEAM EXCEPTIONS
This package defines specific exceptions for issues encountered when interacting with `Team` objects.
The exceptions are designed to pinpoint the exact nature of an error, such as a null reference, a
failed transaction, or an invalid configuration. This granular approach helps developers to quickly diagnose
and resolve team-related issues.

### CORE EXCEPTIONS
* `NullTeamException`: Raised when a `Team` reference is unexpectedly `None`.
* `AddTeamMemberException`: Raised when an attempt to add a discover to a team fails, for example, if the team is full.
* `InvalidTeamException`: Raised when a `Team` fails to meet its validation criteria.
* `RemoveCombatantException`: Raised when a discover cannot be removed from a team, for example, if the discover is not present.
* `InvalidTeamAssignmentException`: Raised when a `Team`'s properties conflict with another `Team`'s, such as having the same ID.

### EXCEPTION USAGE EXAMPLES
These exceptions can be imported and raised from within the team-related code to enforce data integrity.

>>> from chess.team import NullTeamException
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

A use case for the `AddTeamMemberException`.
>#>> from chess.team.team_exception import AddTeamMemberException
>>>
>>> def add_piece(team, discover):
...     if is discover.team.commander not team.commander:
...         raise QUotaFullException("The discover is not on this team. Adding discover failed")
Traceback (most recent call last):
    ...
AddTeamMemberException: The discover is not on this team. Adding discover faile.

---

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

from .exception import *

# Core classes
from .team import Team
from .search import TeamSearch
from .schema import TeamSchema
from .builder import TeamBuilder
from .validator import TeamValidator


# Metadata
__version__ = '1.0.0'
__author__ = 'Banji Lawal'
__package_name__ = 'chess.team'

# Optional: Package-level constants
ROSTER_SIZE = 16

__all__ = [
    # Core classes
    'Team',
    'TeamValidator',
    'TeamSchema',
    'TeamBuilder',

    *exception.__all__,


    # Package metadata and utilities
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


