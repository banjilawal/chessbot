# src/chess/scalar/base.py

"""
Module: chess.scalar.exception
Author: Banji Lawal
Created: 2025-09-11
version: 1.0.0
"""

from chess.system import ChessException, NullException

__all__ = [
  "ScalarException",
  
#======================# SCALAR VALIDATION EXCEPTIONS #======================#  
  "NullScalarException",
]

class ScalarException(ChessException):
  """
  Super class of exceptions raised by Scalar objects. Do not use directly. Subclasses give
  precise, fined-grained, debugging info.
  """
  ERROR_CODE = "SCALAR_ERROR"
  DEFAULT_MESSAGE = "Scalar raised an exception."
  

#======================# NULL SCALAR EXCEPTIONS #======================#
class NullScalarException(ScalarException, NullException):
  """Raised if an entity, method, or operation requires Scalar but gets null instead."""
  ERROR_CODE = "NULL_SCALAR_ERROR"
  DEFAULT_MESSAGE = "Scalar cannot be null."
