# src/chess/system/search/result.py

"""
Module: `chess.system.search.result`
Author: Banji Lawal
Created: 2025-10-04
Updated: 2025-10-10
version: 1.0.0
"""

from typing import Optional, TypeVar, Generic, List

from chess.system import Result

T = TypeVar('T')


class SearchResult(Result[Generic[T]]):
  """
  # ROLE: Message passing, Data Transfer Object

  # RESPONSIBILITIES:
  1. Carry results to the query requestor.
  2. Indicate an empty old_search notification with an object that has neither a payload nor an rollback_exception.

  # PROVIDES:
  Answer from the `Search` service provider containing either:
    1. Matches to the client's query.
    2. An rollback_exception raised during the old_search process or query submission.
    3. A notification containing neither an rollback_exception nor a payload indicating no duplicates were found.

  # ATTRIBUTES:
    * See `Result` superclass for attributes.
  """
  def __init__(self, payload: Optional[List[T]] = None, exception: Optional[Exception] = None):
    super().__init__(payload, exception)



  def __str__(self):
    if self.is_success():
      return f"Result(SUCCESS: {self._payload})"
    elif self.is_empty():
      return "Result(NOT_FOUND)"
    else:
      return f"Result(FAILURE: {self._exception}"





