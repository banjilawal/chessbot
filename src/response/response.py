# src/response/response.py

"""
Module: response.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic,  TypeVar


from request import Request
from response.state import ResponseState


T = TypeVar("T", bound="Request")


class Response(ABC, Generic[T]):
    _request: Request[T]
    _state: ResponseState
    
    def __init__(self, request: Request[T], state: ResponseState):
        self._request = request
        self._state = state
        
    @property
    def request(self) -> Request[T]:
        return self._request
    
    @property
    def state(self) -> ResponseState:
        return self._state
    
    @property
    def is_success(self) -> bool:
        return self._state == ResponseState.SUCCESS

    
    @property
    def is_failure(self) -> bool:
        return self._state == ResponseState.FAILURE
        
    @classmethod
    def success(cls, request: Request[T]) -> Response[T]:
        return cls(request=request, state=ResponseState.SUCCESS)
    
    @classmethod
    def failure(cls, request: Request[T]) -> Response[T]:
        return cls(request=request, state=ResponseState.FAILURE)