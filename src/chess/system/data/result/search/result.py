# src/chess/system/data/result/search/result.py

"""
Module: chess.system.data.result.search.result
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from typing import Generic, List, Optional, TypeVar

from chess.system import DataResult, SearchState, SearchResult

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
        *   state (SearchState)

    # INHERITED ATTRIBUTES:
        *   See DataResult class for inherited attributes.
    """
    _state: SearchState
    
    def __init__(
            self,
            state: SearchState,
            payload: Optional[List[T]] = None,
            exception: Optional[Exception] = None,
    ):
        super().__init__(payload=payload, exception=exception)
        """INTERNAL: Use factory methods instead of direct constructor."""
        method = "TransactionResult.result"
        self._state = state
    
    @property
    def state(self) -> SearchState:
        return self._state
    
    @property
    def is_success(self) -> bool:
        return (
                self.exception is None and
                self.payload is not None and
                self._state == SearchState.SUCCESS
        )
    
    @property
    def is_failure(self) -> bool:
        return (
                self.exception is not None and
                self.payload is None and
                self._state == SearchState.FAILURE
        )
    
    @property
    def is_empty(self) -> bool:
        return (
                self.exception is not None and
                self.payload is None and
                self._state == SearchState.EMPTY
        )
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self.exception is not None and
                self.payload is None and
                self._state == SearchState.TIMED_OUT
        )
    
    @classmethod
    def success(cls, payload: List[T]) -> SearchResult[List[T]]:
        return cls(state=SearchState.SUCCESS, payload=payload)
    
    @classmethod
    def failure(cls, exception: Exception) -> SearchResult[T]:
        return cls(state=SearchState.FAILURE, exception=exception)
    
    @classmethod
    def timed_out(cls, exception: Exception) -> SearchResult[T]:
        return cls(state=SearchState.TIMED_OUT, exception=exception)
    
    @classmethod
    def empty(cls) -> SearchResult[T]:
        return cls(state=SearchState.EMPTY)
