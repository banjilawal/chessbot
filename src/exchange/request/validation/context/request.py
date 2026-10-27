# src/exchange/request/validation/context/request.py

"""
Module: exchange.request.validation.context.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from domain import Context
from exchange import ValidationRequest
from transit import ContextCarrier

T = TypeVar("T", bound="Context")


class ContextValidationRequest(ValidationRequest[T], ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide a ContextValidator job details,

     Attributes:
         id: int
         item: ContextCarrier[T]

     Provides:
     
     Super Class:
        ContextValidationRequest
     """
    _item: ContextCarrier[T]
    
    def __init__(self, id: int, item: ContextCarrier[T]):
        """
        Args:
            id: int
            item: ContextCarrier[T]
        """
        super().__init__(id=id, item=item)
    
    @property
    def item(self) -> ContextCarrier[T]:
        return cast(ContextCarrier[T], super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ContextValidationRequest):
            return self.id == other.id
        return False