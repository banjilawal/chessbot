# src/request/operation/microservice/request.py

"""
Module: request.operation.microservice.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from authorization import OperationRequest
from microservice import Microservice


T = TypeVar("T", bound="Result")


class MicroserviceRequest(OperationRequest[MicroserviceOperation], ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Transport job information throughout the MicroserviceOperation lifecycle.

     Attributes:

     Provides:
     
     Super Class:
        OperationRequest
     """
    _microservice: Microservice
    
    def __init__(self, id: int, microservice: Microservice):
        """
        Args:
            id: int
            microservice: Microservice
        """
        super().__init__(id=id)
        self._microservice = microservice
        
    @property
    def microservice(self) -> Microservice:
        return self._microservice
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, MicroserviceRequest):
            request = cast(MicroserviceRequest, other)
            return self.id == request.id
        return False