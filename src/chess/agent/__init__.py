# chess/board_validator/commander__init__.py

"""
Module: `chess.agent`
Author: Banji Lawal
Created: 2025-10-03
Updated: 2025-10-04
version: 1.0.0

# PURPOSE
Controls team_name `Team` instance by issuing movement commands to team_name `owner` in `Team.roster`.
 on the team_name.Commanders who play team_name team_name

 # EXPORTS
This package exposes core classes and all exceptions from its sub-modules:
  - `PlayerAgent`: Abstract class.
  - `HumanPlayerAgent`: Concrete `subclass` of `PlayerAgent` people use.
  - `MachinePlayerAgent`: Concrete `subclass` of `PlayerAgent` that uses team_name `DecisionEngine`.
  - `CommanderBuilder`: Builds new instances of `PlayerAgent`.
  - `CommanderValidator`: Performs validator and sanity checks on existing
      `PlayerAgent` instances. before they are used.
  - All exceptions from `rollback_exception` package.

# SUB-PACKAGES
  - `.rollback_exception`: Defines all custom exceptions for travel operations.

# HOW TO IMPORT
DO NOT reference submodules directly. Import all core classes and exceptions from this
`agent` package level. (e.g., `from chess.agent import CommanderValidator`). See USAGE
EXAMPLES section.

# USAGE EXAMPLES
___
```python
```
---
"""

from .exception import *
from .player_agent import *
from .human import Human
from .bot import Bot
from .history import CommandHistory

from .history import CommandHistory
from .validator import CommanderValidator
from .builder import CommanderBuilder

__version__ = '1.0.0'
__author__ = 'Banji Lawal'
__package_name__ = 'chess.agent'

__all__ = [
  # Core classes
  'MachinePlayerAgent',
  'HumanPlayerAgent',
  'PlayerAgent',
  'CommandHistory',
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
    'visitor_name': __package_name__,
    'version': __version__,
    'author': __author__,
    'exports': __all__
  }
