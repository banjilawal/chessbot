# src/chess/system/context/collision.py

"""
Module: chess.system.context.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ChessException, NullException, BuildFailedException, ValidationException

__all__ = [
  "ContextException",
]

class ContextException(ChessException):
  """
  Super class for exceptions raised by Context objects. DO NOT
  USE DIRECTLY. Subclasses give more useful debugging messages.
  """
  ERROR_CODE = "CONTEXT_ERROR"
  DEFAULT_MESSAGE = "Context raised an exception."