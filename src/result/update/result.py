# src/result/update/result.py

"""
Module: result.update.result
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain.exchange.response import Response
from result import Result, UpdateState


class UpdateResult(Result[Response]):
    """
    Role:
        -   Data Transport
        -   Error Transport

    Responsibilities:
        1.  Contains the outcome of an update

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
    _state: UpdateState
    _response: Optional[Response]
    _exception: Optional[Exception]

    def __init__(
            self,
            state: UpdateState,
            response: Optional[Response] = None,
            exception: Optional[Exception] = None,
    ):
        """INTERNAL: Use build methods instead of direct constructor."""
        super().__init__(payload=response, exception=exception)
        self._state = state
        
    @property
    def state(self) -> UpdateState:
        return self._state
    
    @property
    def response(self) -> Optional[Response]:
        return cast(Response, super().payload)
    
    @property
    def is_success(self) -> bool:
        return (
            self.response is not None and
            self.exception is None and
            self._state ==  UpdateState.SUCCESS
        )
    
    @property
    def is_failure(self) -> bool:
        return (
                self._response is None and
                self.exception is not None and
                self.state ==  UpdateState.FAILURE or
                self.state ==  UpdateState.TIMED_OUT
        )
    
    @property
    def is_nothing_to_update(self) -> bool:
        return (
                self.response is None and
                self.exception is None and
                self.state ==  UpdateState.NOTHING_TO_UPDATE
        )
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self._response is None and
                self.exception is not None and
                self.state ==  UpdateState.TIMED_OUT
        )
    
    @classmethod
    def success(cls, payload: Response) -> UpdateResult:
        return cls(
            response=payload,
            exception=None,
            state=UpdateState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, exception: Exception) -> UpdateResult:
        return cls(
            response=None,
            exception=exception,
            state=UpdateState.FAILURE,
        )
    
    @classmethod
    def timed_out(cls, exception: Exception) -> UpdateResult:
        return cls(
            response=None,
            exception=exception,
            state=UpdateState.TIMED_OUT,
        )
    
    @classmethod
    def nothing_to_update(cls, ) -> UpdateResult:
        method = f"{cls.__name__}.nothing_to_update"
        return cls(
            response=None,
            exception=None,
            state=UpdateState.NOTHING_TO_UPDATE,
        )

    
