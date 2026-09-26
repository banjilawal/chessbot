# src/exchange/request/validation/request.py

"""
Module: exchange.request.validation.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from artifcat import ValidationResult
from exchange import Request
from transit import EntityCarrier

T = TypeVar("T")

class ValidationRequest(Request[ValidationResult], ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide details about a validation job.

     Attributes:
         id: int
         item: EntityCarrier[T]

     Provides:
     
     Super Class:
        Request
     """
    _item: EntityCarrier[T]
    
    def __init__(
            self,
            id: int,
            item: EntityCarrier[T]
    ):
        """
        Args:
            id: int
            item: EntityCarrier[T]
        """
        super().__init__(id=id)
        self._item = item
        
    @property
    def item(self) -> EntityCarrier[T]:
        return self._item
        
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ValidationRequest):
            return self.id == other.id
        return False