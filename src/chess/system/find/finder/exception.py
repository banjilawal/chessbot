# src/chess/system/find/finder/exception.py

"""
Module: chess.system.find.finder.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import SearchException

__all__ = [
  # ======================# FINDER EXCEPTION #======================#
  "FinderException",
]


# ======================# FINDER EXCEPTION #======================#
class FinderException(SearchException):
  """
  # ROLE: Exception Wrapper, Catchall Exception

  # RESPONSIBILITIES:
  1.  Parent of exception raised by Finder objects.
  3.  Catchall for Finder errors not covered by FinderException subclasses.

  # PARENT:
      *   SearchException

  # PROVIDES:
  None

  # LOCAL ATTRIBUTES:
  None

  # INHERITED ATTRIBUTES:
  None
  """
  ERROR_CODE = "FINDER_ERROR"
  DEFAULT_MESSAGE = "Finder raised an exception."








