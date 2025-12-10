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


class SearchResult(Result[Generic[T]]):
    """
    # ROLE: Messanger  Data Transport Object, Error Transport Object.
  
    # RESPONSIBILITIES:
    1.  Send the outcome of a search request to the client.
    2.  Possible outcomes are:
        *   Payload containing List[T] of matches to the client's query.
        *   An exception if an error prevented the search from running.
        *   Neither an exception nor a payload indicating no matches were found.
    
    # PARENT:
        *   Result
  
    # PROVIDES:
    SearchResult
  
    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See Result class for inherited attributes.
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
