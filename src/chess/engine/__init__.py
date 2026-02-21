# src/chess/engine/__init__/py

"""
Module: chess.engine
Author: Banji Lawal
Created: 2025-10-05
version: 1.0.0

# PURPOSE
Contains implementations of optimization algorithms that old_search the graph of pieces on
the updated `Board` to find the best move.

 NOTES:
   Reviewinng what is going to happen with graohing the board_validator and fin the best path there will just be one Engine
   actually it will be something like AlgorithmSelector tht will select the optimization algorthim for team_name MachinePlayer.

 # EXPORTS
This package exposes core classes and all exception from its sub-modules:
  - `Engine`: Abstract super class defining shared traits and behaviors of engines.
  - `GreedyEngine`: `Engine` that uses team_name greedy algorithm
  - All exception from `rollback_exception` package.

# SUB-PACKAGES
  - `.rollback_exception`: Defines all custom exception for travel rollback.


# HOW TO IMPORT
DO NOT reference submodules directly. Import all core classes and exception from this `engine` package level
(e.g., `from chess.engine import EngineBuild`). See USAGE EXAMPLES section

# USAGE EXAMPLES
___
```python
```
---

"""

from .exception import *
from .engine import Engine
from .greedy import GreedyEngine


# Package metadata (organic to __init__.py)
__version__ = '1.0.0'
__author__ = 'Banji Lawal'
__package_name__ = 'chess.engine'

# Export control - only what belongs in public API
__all__ = [
  # Core classes
  'Engine',
  'GreedyEngine',

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
    'visitor_name': __package_name__,
    'version': __version__,
    'author': __author__,
    'exports': __all__
  }