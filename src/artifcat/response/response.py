# src/client/artifact/response/response.py

"""
Module: client.artifact.response.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar

from artifcat import ResponseState, Result
from client import Request

T = TypeVar("T", bound="Result")


class Response(ABC, Generic[T]):
    """
    Role
        -   Messaging and Transport

    Responsibilities:
        1.  Capture the request-response chain's state and data flow.

    Attributes:
        result: T
        request: Request[T]
        state: ResponseState
        exception: Optional[Exception]
        
    Provides:
        -   is_success: bool
        -   is_failure: bool
        
        -   def success(
                    request: Request[T],
                    result: T,
            ) -> Response[T]:
        
        -   def failure(
                    request: Request[T],
                    result: T,
                    exception: Exception,
            ) -> Response[T]

    Super Class:
    """
    _result: T
    _request: Request[T]
    _state: ResponseState
    _exception: Optional[Exception]
    
    def __init__(
            self,
            result: T,
            request: Request[T],
            state: ResponseState,
            exception: Optional[Exception]
    ):
        """
        Args:
            result: T
            request: Request[T]
            state: ResponseState
            exception: Optional[Exception]
        """
        self._state = state
        self._result = result
        self._request = request
        self._exception = exception or result.exception
        
    @property
    def result(self) -> T:
        return self._result
        
    @property
    def request(self) -> Request[T]:
        return self._request
    
    @property
    def state(self) -> ResponseState:
        return self._state
    
    @property
    def exception(self) -> Optional[Exception]:
        return self._result.exception
    
    @property
    def is_success(self) -> bool:
        return (
            self.result.is_success and
            self.exception is None and
            self._state == ResponseState.SUCCESS
        )
    
    @property
    def is_failure(self) -> bool:
        return not self.success
        
    @classmethod
    def success(
            cls,
            request: Request[T],
            result: T,
    ) -> Response[T]:
        return cls(
            result=result,
            request=request,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(
            cls,
            request: Request[T],
            result: T,
            exception: Exception,
    ) -> Response[T]:
        return cls(
            result=result,
            request=request,
            exception=exception,
            state=ResponseState.FAILURE,
        )