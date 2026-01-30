# src/chess/system/collection/operation/search/result.py

"""
Module: chess.system.collection.operation.search.result
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from __future__ import annotations
from typing import Generic, List, Optional, TypeVar

from chess.system import DataResult, SearchResultEnum, SearchResultState

T = TypeVar("T")


class SearchResult(DataResult[T], Generic[T]):
    """
    # ROLE: Messanger, Data Transport Object, Error Transport Object.

    # RESPONSIBILITIES:
    1.  Send the outcome of a search to the caller.
    2.  Enforcing mutual exclusion. A SearchResult can either carry payload or exception. Not both.

    # PARENT:
        *   DataResult

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   state (DataResultEnum)

    # INHERITED ATTRIBUTES:
        *   See DataResult class for inherited attributes.
    """    
    def __init__(
            self,
            state: SearchResultState,
            exception: Optional[Exception] = None,
            payload: Optional[T] = None,
    ):
        super().__init__(state=state, payload=payload, exception=exception)
        """INTERNAL: Use factory methods instead of direct constructor."""
        method = "SearchResult.result"
    
    @property
    def is_success(self) -> bool:
        return (
                self.payload is not None and
                self.exception is None and
                self.state.classification == SearchResultEnum.SUCCESS
        )
    
    @property
    def is_failure(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state.classification == SearchResultEnum.FAILURE
        )
    
    @property
    def is_empty(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self.state.classification == SearchResultEnum.NOTHING_FOUND
        )
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self.state == SearchResultEnum.TIMED_OUT
        )
    
    @classmethod
    def success(cls, payload: List[T]) -> SearchResult[List[T]]:
        return cls(
            payload=payload,
            exception=None,
            state=SearchResultState(SearchResultEnum.SUCCESS),
        )
    
    @classmethod
    def failure(cls, exception: Exception) -> SearchResult[T]:
        return cls(
            payload=None,
            exception=exception,
            state=SearchResultState(SearchResultEnum.FAILURE),
        )
    
    @classmethod
    def timed_out(cls, exception: Exception) -> SearchResult[T]:
        return cls(
            payload=None,
            exception=exception,
            state=SearchResultState(SearchResultEnum.TIMED_OUT),
        )
    
    @classmethod
    def empty(cls) -> SearchResult[T]:
        return cls(
            payload=None,
            exception=None,
            state=SearchResultState(SearchResultEnum.NOTHING_FOUND),
        )

