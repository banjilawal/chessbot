# src/request/microservice/request.py

"""
Module: request.microservice.request
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from authorization import Request
from microservice import Microservice

T = TypeVar("T", bound="StateModel")


class MicroserviceRequest(Request, ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide information to get permission to run a Microservice operation.

     Attributes:
         id: int
         microservice[T]
         
     Provides:
     
     Super Class:
        Request
     """
    _id: int
    _microservice: Microservice[T]
    
    def __init__(self, id: int, microservice: Microservice[T]):
        """
        Args:
            id: int
            microservice: Microservice[T]
        """
        super().__init__(id)
        self._microservice = microservice
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def microservice(self) -> Microservice[T]:
        return self._microservice
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, MicroserviceRequest):
            request = cast(MicroserviceRequest, other)
            return (
                    super().__eq__(request) and
                    self._microservice.id == request.microservice.id
            )
        return False