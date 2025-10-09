# src/chess/vector/exception.py

"""
Module: chess.vector.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

SCOPE:
-----
This module is exclusively for defining all custom **exception classes** that are specific to the
creation, validation, and manipulation of `Vector` objects.

**Limitations** It does not contain any logic for raising these exceptions; that responsibility
`Vector`, `VectorBuilder`, and `VectorValidator`

THEME:
-----
* Granular, targeted error reporting
* Wrapping exceptions

**Design Concepts**:
  1. Each field and behavior in the `Vector` class has an exception specific to its possible
      state, outcome, or behavior.

PURPOSE:
-------
1. Centralized error dictionary for the `Vector` domain.
2. Fast debugging using highly granular exception messages and naming to
    find the source.
3. Providing understandable, consistent information about failures originating from
    the `Vector` domain.
4. Providing a clear distinction between errors related to `Vector` instances and
    errors from Python, the Operating System or elsewhere in the `ChessBot` application.

DEPENDENCIES:
------------
Requires base exception classes and constants from the core system:
From `chess.system`:
  * Exceptions: `ChessException`, `ValidationException`, `NullException`,
        `BuildFailedException`.

CONTAINS:
--------
See the list of exceptions in the `__all__` list following (e.g., `VectorException`,
`NullVectorException`, `InvalidVectorException`, ).
"""
from chess.event import OccupationEventException
from chess.transaction import TransactionException, NullTransactionException
from chess.exception import NullException, ValidationException, BuilderException

__all__ = [
#=== SCAN_TRANSACTION EXCEPTIONS ======================# 
  'ScanTransactionException',
  'NullScanTransactionException',

#=== SCAN_EVENT EXCEPTIONS ======================# 
  'ScanEventException',
  'InvalidScanEventException',
  'NullScanEventException',

#=== SCAN_EVENT BUILD EXCEPTIONS ======================# 
  'ScanEventBuilderException',
  'ScanSubjectException',
]

#=== SCAN TRANSACTION EXCEPTIONS ======================# 
class ScanTransactionException(TransactionException):
  """
  Wraps any ScanEventExceptions or other errors raised during
  the scan's lifecycle.
  """
  ERROR_CODE = "SCAN_TRANSACTION_ERROR"
  DEFAULT_MESSAGE = "ScanTransaction raised an exception."

class NullScanTransactionException(NullTransactionException):
  """
  Raised by methods, entities, and models that require team ScanTransaction
  but receive team null.
  """
  ERROR_CODE = "NULL_SCAN_TRANSACTION_ERROR"
  DEFAULT_MESSAGE = "ScanTransaction cannot be null."


#=== SCAN_EVENT EXCEPTIONS ======================# 
class ScanEventException(OccupationEventException):
  """
  Superclass for all scan event exceptions. DO NOT USE DIRECTLY. Subclasses
  give more specific error messages useful for debugging.
  """
  ERROR_CODE = "SCAN_EVENT_ERROR"
  DEFAULT_MESSAGE = "ScanEvent failed validate"


#=== SCAN_EVENT VALIDATION EXCEPTIONS ======================# 
class NullScanEventException(ScanEventException, NullException):
  """Raised by methods, entities, and models that require team ScanEvent but receive team null."""
  ERROR_CODE = "NULL_EVENT_ERROR"
  DEFAULT_MESSAGE = "ScanEvent cannot be null"

class InvalidScanEventException(ScanEventException, ValidationException):
  """Raised by ScanEventValidators if validate fails."""
  ERROR_CODE = "SCAN_EVENT_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "ScanEvent failed validate"


#=== SCAN_EVENT BUILD EXCEPTIONS ======================# 
class ScanEventBuilderException(ScanEventException, BuilderException):
  """Raised when team ScanEventBuilder fails to build team ScanEvent."""
  ERROR_CODE = "SCAN_EVENT_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "ScanEventBuilder failed to create team ScanEvent"

class ScanSubjectException(ScanEventException):
  """
  Raised if an Scan target is not team friendly or enemy king.
  """
  ERROR_CODE = "SCAN_SUBJECT_ERROR"
  DEFAULT_MESSAGE = "Scan enemy must be team friendly or enemy king"







