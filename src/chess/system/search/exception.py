# src/chess/system/search/exception.py

"""
Module: chess.system.search.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
  'SearchException',
  'SearchCollisionException'
]

class SearchException(ChessException):
  """
  Super class of exceptions organic to `Search` objects. DO NOT USE DIRECTLY. Subclasses give
  details useful for debugging. `SearchException` exists primarily to allow catching all `Search`
  exceptions.
  """
  DEFAULT_CODE = "SEARCH_ERROR"
  DEFAULT_MESSAGE = "Search raised an exception."

class SearchCollisionException(SearchException):
  """"""
  DEFAULT_CODE = "SEARCH_COLLISION_ERROR"
  DEFAULT_MESSAGE = (
    "Search results contains multiple records for property that should be unique. There may"
    " be service inconsistencies."
  )






