# src/artifact/response/response.py

"""
Module: artifact.response.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar

from artifcat import ResponseState, Result
from exchange import Request

T = TypeVar("T")


class Response(ABC, Generic[T]):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a request-response cycle's data and state.

    Attributes:
        request: Request[T]
        state: ResponseState
        result: Optional[Result[T]]
        exception: Optional[Exception]
        
    Provides:
        -   is_success: bool
        -   is_failure: bool
        
        -   def success(request: Request[T], result: Result[T]) -> Response[T]:
        
        -   def failure(request: Request[T], exception: Exception) -> Response[T]

    Super Class:
    """
    _request: Request[T]
    _state: ResponseState
    _result: Optional[T]
    _exception: Optional[Exception]
    
    def __init__(
            self,
            request: Request[T],
            state: ResponseState,
            result: Optional[T] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            request: Request[T]
            state: ResponseState
            result: Optional[T]
            exception: Optional[Exception]
        """
        self._state = state
        self._result = result
        self._request = request
        self._exception = exception
    
    @property
    def state(self) -> ResponseState:
        return self._state
        
    @property
    def request(self) -> Request[T]:
        return self._request
    
    @property
    def result(self) -> Optional[T]:
        return self._result
    
    @property
    def exception(self) -> Optional[Exception]:
        return self._exception
    
    @property
    def is_success(self) -> bool:
        return (
            self._exception is None and
            self._result is not None and
            self._request is not None and
            self._result.is_success and
            self._state == ResponseState.SUCCESS
        )
    
    @property
    def is_failure(self) -> bool:
        return not self.success
        
    @classmethod
    def success(cls, result: T, request: Request[T]) -> Response[T]:
        return cls(
            result=result,
            request=request,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, request: Request[T], exception: Exception) -> Response[T]:
        return cls(
            request=request,
            exception=exception,
            state=ResponseState.FAILURE,
        )