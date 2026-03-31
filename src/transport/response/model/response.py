# src/transport/response/model/response.py

"""
Module: transport.response.model.response
Author: Banji Lawal
Created: 2026-03-30
version: 1.0.0
"""

from __future__ import annotations

from response import Response
from logic.system import Result
from transport import ServiceRequest


class Response:
    _id: int
    _request: ServiceRequest
    _result: Result
    
    def __init__(self, id: int, request: ServiceRequest, response: Response):
        """
        Args:
            id: int
            request: ServiceRequest
            response: Response
        """
        self._id = id
        self._request = request
        self._response = response
        
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def request(self) -> ServiceRequest:
        return self._request
    
    @property
    def response(self) -> Response:
        return self._response
    
    def __eq__(self, other: object) -> bool:
        if other is self: return True
        if other is None: return False
        if isinstance(other, Response):
            return self._id == other._id
        return False
        