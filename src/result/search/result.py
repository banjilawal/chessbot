# src/result/search/result.py
"""
Module: result.search.result
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Generic, List, Optional, TypeVar

from result import Result, SearchState

T = TypeVar("T")


class SearchResult(Result[T], Generic[T]):
    """
    Role:
        -   Data Transport
        -   Error Transport

    Responsibilities:
        1.  Contains the outcome of a search transaction

    Attributes:
        exception: Optional[Exception]
        payload: Optional[T]
        state: SearchState
        is_timed_out: bool
        is_success: bool
        is_failure: bool
        is_empty: bool

    Provides:
        -   def empty() -> SearchResult[T]:
        -   def success(payload: T) -> Result[T]
        -   def failure(exception: Exception) -> Result[T]
        -   def timed_out(cls, exception: Exception) -> SearchResult[T]:

    Super Class:
        Result
    """
    _state: SearchState
    
    def __init__(
            self,
            state: SearchState,
            payload: Optional[T] = None,
            exception: Optional[Exception] = None,
    ):
        """
        Args:
            state: SearchState
            payload: Optional[T]
            exception: Optional[Exception]
        """
        super().__init__(payload=payload, exception=exception)
        """INTERNAL: Use Search methods instead of direct constructor."""
        self._state = state
        
    @property
    def state(self) -> SearchState:
        return self._state
    
    @property
    def is_success(self) -> bool:
        return (
                self.payload is not None and
                self.exception is None and
                self._state == SearchState.SUCCESS
        )
    
    @property
    def is_failure(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state == SearchState.FAILURE
        )
    
    @property
    def is_empty(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state == SearchState.NOTHING_FOUND
        )
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state == SearchState.TIMED_OUT
        )
    
    @classmethod
    def success(cls, payload: List[T]) -> SearchResult[List[T]]:
        return cls(
            payload=payload,
            exception=None,
            state=SearchState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, exception: Exception) -> SearchResult[T]:
        return cls(
            payload=None,
            exception=exception,
            state=SearchState.FAILURE,
        )
    
    @classmethod
    def timed_out(cls, exception: Exception) -> SearchResult[T]:
        return cls(
            payload=None,
            exception=exception,
            state=SearchState.TIMED_OUT,
        )
    
    @classmethod
    def empty(cls) -> SearchResult[T]:
        return cls(
            payload=None,
            exception=None,
            state=SearchState.NOTHING_FOUND,
        )

