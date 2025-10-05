# chess/board/commander__init__.py

"""
Module: `chess.commander`
Author: Banji Lawal
Created: 2025-10-03
Updated: 2025-10-04
version: 1.0.0

# PURPOSE
Controls a `Team` instance by issuing movement commands to a `piece` in `Team.roster`.
 on the team.Commanders who play a team

 # EXPORTS
This package exposes core classes and all exceptions from its sub-modules:
  - `Commander`: Abstract class.
  - `Human`: Concrete `subclass` of `Commander` people use.
  - `Bot`: Concrete `subclass` of `Commander` that uses a `DecisionEngine`.
  - `CommanderBuilder`: Builds new instances of `Commander`.
  - `CommanderValidator`: Performs validation and sanity checks on existing
      `Commander` instances. before they are used.
  - All exceptions from `exception` package.

# SUB-PACKAGES
  - `.exception`: Defines all custom exceptions for occupation operations.

# HOW TO IMPORT
DO NOT reference submodules directly. Import all core classes and exceptions from this
`commander` package level. (e.g., `from chess.commander import CommanderValidator`). See USAGE
EXAMPLES section.

# USAGE EXAMPLES
___
```python
```
---
"""

from .exception import *
from .commander import *
from .human import Human
from .bot import Bot
from .history import CommandHistory

from .history import CommandHistory
from .validator import CommanderValidator
from .builder import CommanderBuilder

__version__ = '1.0.0'
__author__ = 'Banji Lawal'
__package_name__ = 'chess.commander'

__all__ = [
  # Core classes
  'Bot',
  'Human',
  'Commander',
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
    'name': __package_name__,
    'version': __version__,
    'author': __author__,
    'exports': __all__
  }
