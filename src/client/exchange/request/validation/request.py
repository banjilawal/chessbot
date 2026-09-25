# src/client/exchange/request/validation/request.py

"""
Module: client.exchange.request.validation.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from client import Request
from transit import EntityCarrier

T = TypeVar("T")



class ValidationRequest(Request[T], ABC, Generic[T]):
    """
     Role:
         - Messaging
         - Transport

     Responsibilities:
        1. Transport the collection and other objects a ValidationOperation needs to run a job.

     Attributes:
         id: int

     Provides:
     
     Super Class:
        Request
     """
    
    def __init__(self, id: int):
        """
        Args:
            id: int
        """
        super().__init__(id=id)
        
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ValidationRequest):
            return self.id == other.id
        return False