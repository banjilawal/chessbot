# src/chess/system/find/result.py

"""
Module: chess.system.find.result
Author: Banji Lawal
Created: 2025-10-04
Updated: 2025-10-10
version: 1.0.0
"""

from typing import Optional, TypeVar, Generic, List

from chess.system import Result

T = TypeVar("T")


class SearchResult(Result[List[Generic[T]]]):
    """
    # ROLE: Message passing, Data Transfer Object
  
    # RESPONSIBILITIES:
    1.  Carry results to the query requestor.
  
    # PROVIDES:
    Answer from the Finder containing either:
        *   Payload containing List[T] of matches to the client's query.
        *   An exception indicating a error occurred during the search.
        *   Neither an exception nor a payload indicating no matches were found.
  
    # ATTRIBUTES:
      * See Result superclass for attributes.
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
