# src/exchange/request/validation/struct/register/request.py

"""
Module: exchange.request.validation.struct.register.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from domain import Register
from exchange import StructValidationRequest
from transit import RegisterCarrier

T = TypeVar("T", bound="Register")


class RegisterValidationRequest(StructValidationRequest[T], ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Transport the collection and other objects a RegisterValidator needs to run a job.

     Attributes:
         id: int
         item: T

     Provides:
     
     Super Class:
        ValidationRequest
     """
    
    def __init__(self, id: int, item: RegisterCarrier[T]):
        """
        Args:
            id: int
            item: RegisterCarrier[T]
        """
        super().__init__(id=id, item=item)
    
    @property
    def item(self) -> RegisterCarrier[T]:
        return cast(RegisterCarrier[T], super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, RegisterValidationRequest):
            return self.id == other.id
        return False