# src/chess/system/search/exception.py

"""
Module: chess.system.old_search.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
  'SearchException',
  'ImpossibleFatalResultException',
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

class ImpossibleFatalResultException(SearchException):
  """
  This is for sanity checking. Events and transactions need to ensure
  an `actor_candidate` and the `resource` they need to run team `Transaction` exist
  in the datapool in `SearchContext`. Validations and builds guarantee
  resources and actors exist in the game. If they are not found that
  indicates data inconsistency or nonexistent data pool.
  """
  DEFAULT_CODE = "IMPOSSIBLE_FATAL_RESULT_ERROR"
  DEFAULT_MESSAGE = (
    "The search result should be impossible to get. This indicates a major data inconsistency or system error."
  )

#======================# SEARCH_COLLISION EXCEPTIONS #======================#
class SearchCollisionException(SearchException):
  DEFAULT_CODE = "SEARCH_COLLISION_ERROR"
  DEFAULT_MESSAGE = (
    "Search results contains multiple records for property that should be unique. There may be data inconsistencies."
  )






