# src/request/microservice/token/request.py

"""
Module: request.microservice.token.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from typing import cast

from authorization import MicroserviceRequest
from microservice import TokenService
from model import Token


class TokenServiceRequest(MicroserviceRequest[Token]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Transport job information to a worker.

     Attributes:
        id: int
        microservice: TokenService

     Provides:
     
     Super Class:
        MicroserviceRequest
     """
    
    def __init__(self, id: int, microservice: TokenService):
        """
        Args:
            id: int
            microservice: TokenService
        """
        super().__init__(id=id, microservice=microservice)
        
    @property
    def microservice(self) -> TokenService:
        return cast(TokenService, super().microservice)
        
        
    
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, MicroserviceRequest):
            return super().__eq__(other)
        return False