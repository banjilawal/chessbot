# src/message/response/response.py

"""
Module: message.response.response
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

T = TypeVar("T", bound="Request")

class Response(ABC, Generic[T]):
    _request: T
    
    def __init__(self, request: T):
        self._request = request
        
    @property
    def request(self) -> T:
        return self._request
    
    def __eq__(self, other) -> bool:
        if other is self:
            return True
        if other is None:
            return False
        if isinstance(other, Response):
            response = cast(Response, other)
            return self.request == response.request
        return False