"""
chess.commander Package

PURPOSE:
    Commaners who play a team

CORE CLASSES:
    Commander
    HumanCommander
    CyberneticCompettor

PURPOSE:
    Contains core commander team_exception classes and coordinate utilities.


COMMANDER EXCEPTIONS CLASSES:
    NullCommanderException
    CommandervalidationException

USAGE:
    >>>
    >>>

VERSION: 1.0.0
AUTHOR: Banji L
"""

from .exception import *

from .commander import Commander
from .human_commander import HumanCommander
from .cybernetic_commander import CyberneticCommander
from .team_list import TeamList
from .commander_type import CommanderType
from .commander_validator import CommanderValidator
from .commander_builder import CommanderBuilder

__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.commander"

__all__ = [
    # Core classes
    'Commander',
    'HumanCommander',
    'CyberneticCommander',
    'TeamList',
    'CommanderType',
    'CommanderValidator',
    'CommanderBuilder',

    *exception.__all__,


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
