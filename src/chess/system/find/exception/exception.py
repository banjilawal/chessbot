# src/chess/system/find/exception/exception.py

"""
Module: chess.system.find.exception.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
  # ======================# FINDER EXCEPTION #======================#
  "FinderException",
]


# ======================# FINDER EXCEPTION #======================#
class FinderException(ChessException):
  """
  # ROLE: Exception Wrapper, Catchall Exception

  # RESPONSIBILITIES:
  1.  Parent of exception raised by Finder objects
  3.  Catchall for Finder errors not coveredby lower level  Finder exception.

  # PARENT:
      *   ChessException

  # PROVIDES:
  FinderException

  # LOCAL ATTRIBUTES:
  None

  # INHERITED ATTRIBUTES:
  None
  """
  DEFAULT_CODE = "FINDER_ERROR"
  DEFAULT_MESSAGE = "Finder raised an exception."








