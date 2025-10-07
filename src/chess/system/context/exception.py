# src/chess.context.exception.py

"""
Module: chess.context.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

SCOPE:
-----
This module is exclusively for defining all custom **exception classes** that are specific to the
creation, validation, and manipulation of **Context objects**. It handles boundary checks (row/column)
limits and null checks. It does not contain any logic for *raising* these exceptions; that responsibility
falls to the `ContextValidator` and `ContextBuilder`processes.

THEME:
-----
**Comprehensive Domain Error Catalog.** The central theme is to provide a
highly granular and hierarchical set of exceptions, ensuring that callers can
catch and handle errors based on both the **type of failure** (e.g., `NullException`)
and the **affected domain** (e.g., `ContextException`). This enables precise error
logging and handling throughout the system.

PURPOSE:
-------
To serve as the **centralized error dictionary** for the `Context` domain.
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
See the list of exceptions in the `__all__` list following (e.g., `ContextException`,
`NullContextException`, `RowAboveBoundsException`).
"""

from chess.system import ChessException, NullException, BuildFailedException, ValidationException

__all__ = [
  'ContextException',

#======================#  CONTEXT VALIDATION EXCEPTIONS ======================# 
  'NullContextException',
  'InvalidContextException',

#======================#  CONTEXT BUILD EXCEPTIONS ======================# 
  'ContextBuildFailedException',
]

class ContextException(ChessException):
  """
  Super class for exceptions raised by Context objects. DO NOT
  USE DIRECTLY. Subclasses give more useful debugging messages.
  """
  ERROR_CODE = "CONTEXT_ERROR"
  DEFAULT_MESSAGE = "Context raised an exception"

#======================#  CONTEXT VALIDATION EXCEPTIONS ======================# 
class NullContextException(ContextException, NullException):
  """
  Raised if an entity, method, or operation requires a context but
  gets null instead.
  """
  ERROR_CODE = "NULL_CONTEXT_ERROR"
  DEFAULT_MESSAGE = f"Context cannot be null"

class InvalidContextException(ContextException, ValidationException):
  """
  Raised by contextBValidator if context fails sanity checks. Exists primarily to
  catch all exceptions raised validating an existing context
  """
  ERROR_CODE = "CONTEXT_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Context validation failed."

#======================#  CONTEXT BUILD EXCEPTIONS ======================# 
class ContextBuildFailedException(ContextException, BuildFailedException):
  """
  Raised when ContextBuilder encounters an error while building a team.
  Exists primarily to catch all exceptions raised build a new context
  """
  ERROR_CODE = "CONTEXT_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "Context build failed."