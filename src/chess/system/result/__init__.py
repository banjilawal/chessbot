# chess/system/result/__init__.py

"""
Module: chess.system.result
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0

# PURPOSE
Interface for data-holding objects which represent outcome of operations that produce one of two
results only.
    * Success: A payload is returned
    * Failure: An exception is raised

# EXPORTS
This package exposes core classes and all exceptions from its sub-modules:
    - `Result`: Abstract super class.
    - All exceptions from `exception` package.

### USAGE EXAMPLES
These examples show recommended workflows with `Result` and `BuildResult`.
---
```python
from chess.system.result import Result, BuildResult

# Example of a successful operation
def add(x, y) -> Result[int]:
    if x is None:
        return Result(err=ValueError("x cannot be None"))
    if y is None:
        return Result(err=ValueError("x cannot be None"))

    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return Result(err=TypeError(Value"parameters must be numbers"))
    return Result(payload=(x + y))

# Example of a failed build operation

```python

```
---
"""

from .exception import *
from .result import Result
from .transaction import TransactionResult


# Package metadata (organic to __init__.py)
__version__ = '1.0.0'
__author__ = 'Banji Lawal'
__package_name__ = 'chess.system.result'

# Export control - only what belongs in public API
__all__ = [
    'Result',
    'TransactionResult',

    *exception.__all__,

    '__version__',
    '__author__',
    'package_info',
]

# Organic utility function for package info
def package_info() -> dict:
    '''Return basic package information.'''
    return {
        'name': __package_name__,
        'version': __version__,
        'author': __author__,
        'exports': __all__
    }
