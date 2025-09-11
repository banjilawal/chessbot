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

>>> from chess.team import Team, TeamProfile, TeamValidator
>>> # Create a new team and roster
>>> team = Team(team_id=1, commander=white_team_commander, profile=TeamProfile.WHITE)
>>> validation = TeamValidator.validate(team)
---

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

# Subpackages
from .exception import *

# Core classes
from .team import Team
from .team_roster import TeamRoster
from .team_profile import TeamProfile
from .team_validator import TeamValidator

# Metadata
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.team"

# Optional: Package-level constants
ROSTER_SIZE = 16

__all__ = [
    # Core classes
    "Team",
    "TeamRoster",
    "TeamValidator",
    "TeamProfile",

    # Subpackages
    *exception.__all__,
    "exception",

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


