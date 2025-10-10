# src/chess/system/transaction/exception.py

"""
Module: chess.system.event.transaction.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

SCOPE:
-----
This module is exclusively for defining all custom **exception classes** that are specific to the
creation, validation, and manipulation of **Coord objects**. It handles boundary checks (row/column)
limits and null checks. It does not contain any logic for *raising* these exceptions; that responsibility
falls to the `CoordValidator` and `CoordBuilder`processes.

THEME:
-----
**Comprehensive Domain Error Catalog.** The central theme is to provide team
highly granular and hierarchical set of exceptions, ensuring that callers can
catch and handle errors based on both the **type of failure** (e.g., `NullException`)
and the **affected domain** (e.g., `CoordException`). This enables precise error
logging and handling throughout the system.

PURPOSE:
-------
To serve as the **centralized error dictionary** for the `Coord` domain.
It abstracts underlying Python exceptions into domain-specific, custom error types
to improve code clarity and facilitate robust error handling within the chess engine.

DEPENDENCIES:
------------
Requires base exception classes and constants from the core system:
From `chess.system`:
  * Constants: `ROW_SIZE`, `COLUMN_SIZE`
  * Exceptions: `ChessException`, `ValidationException`, `NullException`,
        `BuildFailedException`.

CONTAINS:
--------
See the list of exceptions in the `__all__` list following (e.g., `CoordException`,
`NullCoordException`, `RowAboveBoundsException`).
"""

from chess.system import ChessException, ValidationException, NullException, BuildFailedException

__all__ = [
  'TransactionException',

#======================# TRANSACTION VALIDATION EXCEPTIONS #======================#
  'NullTransactionException',
  'InvalidTransactionException'
]



class TransactionException(ChessException):
  """
  Super class of all exceptions `Transaction` object raises. Do not use directly. Subclasses give
  details useful for debugging. This class exists primarily to allow catching all `Transaction`
  exceptions.
  """
  ERROR_CODE = "TRANSACTION_ERROR"
  DEFAULT_MESSAGE = "Transaction raised an exception."


#======================# TRANSACTION VALIDATION EXCEPTIONS #======================#
class NullTransactionException(TransactionException, NullException):
  """Raised if an entity, method, or operation requires `Transaction` but gets null instead."""
  ERROR_CODE = "NULL_TRANSACTION_ERROR"
  DEFAULT_MESSAGE = "Transaction cannot be null"

class InvalidTransactionException(TransactionException, ValidationException):
  """
  Raised by `TransactionValidator` if an object fails sanity checks. Exists primarily to catch all
  exceptions raised validating an existing`Transaction`.
  """
  ERROR_CODE = "TRANSACTION_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Transaction validation failed"
