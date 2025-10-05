# src/chess/system/search/exception.py

"""
Module: `chess.system.search.exception`
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
Responsibilities: Holds exceptions organic to `Search` objects

Contains:
See the list of exception in the `__alL__` list following
"""

from chess.system import ChessException

__all__ = [
  'SearchException',
  'SearchParamException',
  'ImpossibleFatalResultException'
]

class SearchException(ChessException):
  """
  Super class of exceptions organic to `Search` objects. DO NOT USE DIRECTLY. Subclasses give
  details useful for debugging. `SearchException` exists primarily to allow catching all `Search`
  exceptions.
  """
  DEFAULT_CODE = "SEARCH_ERROR"
  DEFAULT_MESSAGE = "Search raised an exception."


class SearchParamException(SearchException):
  """
  This is different than failed validation checks. Might not be
  necessary.
  """
  DEFAULT_CODE = "SEARCH_PARAM_ERROR"
  DEFAULT_MESSAGE = "Search parameters raised an exception."


class ImpossibleFatalResultException(SearchException):
  """
  This is for sanity checking. Events and transactions need to ensure
  an `actor` and the `resource` they need to run a `Transaction` exist
  in the datapool in `SearchContext`. Validations and builds guarantee
  resources and actors exist in the game. If they are not found that
  indicates data inconsistency or nonexistent data pool.
  """
  DEFAULT_CODE = "IMPOSSIBLE_FATAL_RESULT_ERROR"
  DEFAULT_MESSAGE = (
    "The search result should be impossible. The result "
    "indicates a major data inconsistency or system error"
  )








