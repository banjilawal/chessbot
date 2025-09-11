"""
chess.commander Package

PURPOSE:
    Commaners who play a team

CORE CLASSES:
    Commander
    HumanCommander
    CyberneticCompettor

USAGE:
    >>>
    >>>

VERSION: 1.0.0
AUTHOR: Banji L
"""

from .exception import *

from .commander import Commander
from .human import HumanCommander
from .cybernetic import CyberneticCommander
from .teams_commanded import TeamsCommanded
from .commander_type import CommanderType
from .commander_validator import CommanderValidator

__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.commander"

__all__ = [
    # Core classes
    "Commander",
    "HumanCommander",
    "CyberneticCommander",
    "TeamsCommanded",
    "CommanderType",
    "CommanderValidator",

    # Subpackages
    *exception.__all__,
    "exception",

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
