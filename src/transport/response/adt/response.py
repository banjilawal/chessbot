# src/transport/result/model/result.py

"""
Module: transport.result.model.result
Author: Banji Lawal
Created: 2026-03-30
version: 1.0.0
"""

from __future__ import annotations


from system import Result
from transport import ServiceRequest


class Response:
    _id: int
    _request: ServiceRequest
    _result: Result
    
    def __init__(self, id: int, request: ServiceRequest, result: Result):
        """
        Args:
            id: int
            result: Result
            request: ServiceRequest
        """
        self._id = id
        self._request = request
        self._result = result
        
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def request(self) -> ServiceRequest:
        return self._request
    
    @property
    def result(self) -> Result:
        return self._result
    
    def __eq__(self, other: object) -> bool:
        if other is self: return True
        if other is None: return False
        if isinstance(other, Response):
            return other.id == self._id
        return False
        