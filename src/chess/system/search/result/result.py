# src/chess/system/search/result.py

"""
Module: `chess.system.search.result`
Author: Banji Lawal
Created: 2025-10-04
Updated: 2025-10-10
version: 1.0.0

# SECTION 1 - Purpose:
This module provides:
  1. A satisfaction of the `ChessBot` reliability requirement.
  2. A satisfaction of the performance requirement.

# SECTION 2 - Scope:
The module covers clients servers, and data owners in the `ChessBot` search domain.

# SECTION 3 - Limitations:
  1. The module is limited to presenting the answer from a `Search` service provider to the client delivering a query.
  2. The module does not guarantee the accuracy or precision of data in the result.

# SECTION 4 - Design Considerations and Themes:
The major theme influencing the modules design are
  1. Single responsibility.
  2. A consistent interface aiding discoverability, understanding and simplicity.

# SECTION 5 - Features Supporting Requirements:
  1. The ability to handle errors without crashing the application is a reliability feature.
  2. Performance does not degrade under high search loads.

# 6 Feature Delivery Mechanism:
  1. The module implements logic for carrying either an exception or result of a successful search. in the same
      container. This improves resource.
  2. Delivering an exception in the return instead of raising gives application higher reliability, uptimes and
      survivability.

# SECTION 7 - Dependencies:
* From `chess.system`:
    `Result`

* From Python `typing` Library:
    `Generic`, `TypeVar`, `Optional`

# SECTION 8 - Contains:
1. `SearchResult`
"""

from typing import Optional, TypeVar, Generic, List

from chess.system import Result

T = TypeVar('T')


class SearchResult(Result[Generic[T]]):
  """
  # ROLE: Message passing, Data Transfer Object

  # RESPONSIBILITIES:
  1. Carry results to the query requestor.
  2. Indicate an empty search result with an object that has neither a payload nor an exception.

  # PROVIDES:
  Answer from the `Search` service provider containing either:
    1. Matches to the client's query.
    2. An exception raised during the search process or query submission.
    3. A result containing neither an exception nor a payload indicating no matches were found.

  # ATTRIBUTES:
    * See `Result` superclass for attributes.
  """
  def __init__(self, payload: Optional[List[T]] = None, exception: Optional[Exception] = None):
    super().__init__(payload, exception)


  def is_success(self) -> bool:
    """
    # ACTION:
    Confirm if a search produced at least one hit.

    # PARAMETERS:
      No parameters

    # RETURNS:
      `bool`

    RAISES:
      No exception raised.
    """
    method = "SearchResult.is_success"
    return self.exception is None and self.payload is not None


  def is_empty(self) -> bool:
    """
    # ACTION:
    Confirm if a search produced no hits.

    # PARAMETERS:
      No parameters

    # RETURNS:
      `bool`

    RAISES:
      No exceptions raised.
    """
    method = "is_empty"
    return self._exception is None and self._payload is None


  def __str__(self):
    if self.is_success():
      return f"Result(SUCCESS: {self._payload})"
    elif self.is_empty():
      return "Result(NOT_FOUND)"
    else:
      return f"Result(FAILURE: {self._exception}"





