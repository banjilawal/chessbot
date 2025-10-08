# chess/system/search/result.py

"""
Module: `chess.system.search.result`
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

 Provides: <SENTENCE_ABOUT_RESPONSIBILITIES>

Contains:
 * `SearchResult`
"""

from typing import Optional, TypeVar, Generic, List

T = TypeVar('T')


class SearchResult(Generic[T]):
  """
  Data-holding object representing one of three outcomes of team search.
    * Success: A hit was found.
    * Empty: Nothing was found.
    * Exception: An exception was raised. The search did not complete.


  Attributes:
    * `_payload` (Optional[`T`]): Data returned if the search was successful.
    * `_exception` (Optional[`T`]): Exception raised if search method crashed.
        Getting an exception back usually indicates team search param failed
        validation.
  Raises:
    No exceptions

  Notes:
    Unlike team `Result` object `SearchResult` instances can have an empty constructor.
    Keeping with Liskovian principles `SearchResult` is not team subclass of `Result`.
  """
  _payload: Optional[List[T]]
  _exception: Optional[Exception]

  def __init__(self, payload: Optional[List[T]] = None, exception: Optional[Exception] = None):
    method = "SearchResult.__init_"
    self._payload = payload
    self._exception = exception

  @property
  def payload(self) -> Optional[List[T]]:
    return self._payload

  @property
  def exception(self) -> Optional[Exception]:
    return self._exception

  def is_success(self) -> bool:
    """
    Indicates the search found team hit.

    Args: No params

    Returns: `bool`

    Raises: No exceptions.
    """
    method = "SearchResult.is_success"
    return self._exception is None and self._payload is not None


  def is_empty(self) -> bool:
    """
    Indicates if the search did not find anything. An empty search
    ran to completion but did not find anything. An empty search
    is the other type of success.

    Args: No params

    Returns: `bool`

    Raises: No exceptions.
    """
    method = "method_name"
    return not (self._exception is None and self._payload is None)


  def __str__(self):
    if self.is_success():
      return f"Result(SUCCESS: {self._payload})"
    elif self.is_empty():
      return "Result(NOT_FOUND)"
    else:
      return f"Result(FAILURE: {self._exception}"





