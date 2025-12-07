# src/chess/system/searcher/base.py

"""
Module: chess.system.searcher.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
  "FinderException",
]

class FinderException(ChessException):
  """
  Super class of exceptions organic to `Finder` objects. DO NOT USE DIRECTLY. Subclasses give
  details useful for debugging. `FinderException` exists primarily to allow catching all `Finder`
  exceptions.
  """
  DEFAULT_CODE = "FINDER_ERROR"
  DEFAULT_MESSAGE = "Finder raised an exception."








