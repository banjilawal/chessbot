# src/client/artifact/response/response.py

"""
Module: client.artifact.response.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic,  TypeVar

from artifcat import Result
from client import Request, ResponseState

T = TypeVar("T", bound="Result")


class Response(ABC, Generic[T]):
    _result: T
    _request: Request[T]
    _state: ResponseState
    
    def __init__(
            self,
            result: T,
            request: Request[T],
            state: ResponseState
    ):
        """
        Args:
            result: T
            request: Request[T]
            state: ResponseState
        """
        self._result = result
        self._request = request
        self._state = state
        
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
    def is_success(self) -> bool:
        return (
            self.result.is_success and
            self._state == ResponseState.SUCCESS
        )

    
    @property
    def is_failure(self) -> bool:
        return (
            self._result.is_failure and
            self._state == ResponseState.FAILURE
        )
        
    @classmethod
    def success(cls, result: T, request: Request[T],) -> Response[T]:
        return cls(
            result=result,
            request=request,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, result: T, request: Request[T],) -> Response[T]:
        return cls(
            result=result,
            request=request,
            state=ResponseState.FAILURE,
        )