# src/exchange/request/validation/structure/request.py

"""
Module: exchange.request.validation.structure.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Any, Generic, TypeVar, cast

from domain import Structure
from exchange import ValidationRequest
from transit import StructureCarrier

T = TypeVar("T", bound="Structure")

class StructureValidationRequest(ValidationRequest[T], ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Transport the collection and other objects a ValidationOperation needs to run a job.

     Attributes:
         id: int
         item: Any

     Provides:
     
     Super Class:
        ValidationRequest
     """
    
    def __init__(self, id: int, item: StructureCarrier[T]):
        """
        Args:
            id: int
            item: StructureCarrier[T]
        """
        super().__init__(id=id)
        self._item = item
    
    @property
    def item(self) -> StructureCarrier[T]:
        return cast(StructureCarrier[T], super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, StructureValidationRequest):
            return self.id == other.id
        return False