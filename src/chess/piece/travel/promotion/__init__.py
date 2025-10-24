# src/chess/travel/promotion/__init__.py

"""
Module: chess.travel.promotion
Author: Banji Lawal
Created: 2025-10-05
version: 1.0.0


# PURPOSE
Objects and utilities responsible for the Promotion lifecycle.



 # EXPORTS
This package exposes core classes and all exceptions from its sub-modules:
  - `PromotionEvent`: Information necessary to fire the notification.
  - `PromotionTransaction`: Runs the promotion lifecycle.
  - `PromotionEventBuilder: Safely creates the `PromotionEvent`
  - `PromotionEventValidator`
  - All exceptions from `rollback_exception` package.

# SUB-PACKAGES
  - `.rollback_exception`: Defines all custom exceptions for travel operations.
  - `.ADDITIONAL_SUB_PACKAGE`: Logic for capturing, promoting, castling, and moving pieces on `Board`.

# HOW TO IMPORT
DO NOT reference submodules directly. Import all core classes and exceptions from this `board_validator` package level
(e.g., `from chess.board_validator import InvalidBoardException`). See USAGE EXAMPLES section

# USAGE EXAMPLES
___
```python
```
---

# BEST PRACTICES
 1. <BEST_PRACTICE_1>
"""

from .exception import *

# Package metadata (organic to __init__.py)
__version__ = '1.0.0'
__author__ = 'Banji Lawal'
__package_name__ = 'chess.system.build'

# Export control - only what belongs in public API
__all__ = [
  # Core classes
  'Builder',
  'BuildResult',
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
    'name': __package_name__,
    'version': __version__,
    'author': __author__,
    'exports': __all__
  }