# chess/board/commander__init__.py

"""
Module: `chess.commander`
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0

## PURPOSE
    Commaners who play a team

## CORE CLASSES
    Commander
    Human
    CyberneticCompettor

## PURPOSE
    Contains core commander team_exception classes and coordinate utilities.


COMMANDER EXCEPTIONS CLASSES:
    NullCommanderException
    CommandervalidationException

USAGE:
    >>>
    >>>
"""

from .exception import *
from .commander import *

from .team_list import TeamList
from .validator import CommanderValidator
from .builder import CommanderBuilder

__version__ = '1.0.0'
__author__ = 'Banji Lawal'
__package_name__ = 'chess.commander'

__all__ = [
    # Core classes
    'TeamList',
    'CommanderValidator',
    'CommanderBuilder',

    *commander.__all__,
    *exception.__all__,


    '__version__',
    '__author__',
    'package_info'
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
