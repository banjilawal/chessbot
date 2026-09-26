# src/exchange/request/validation/structure/request.py

"""
Module: exchange.request.validation.structure.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any

from exchange import Structure, ValidationRequest

class StructureValidationRequest(ValidationRequest[Structure]):
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
    _item: Any
    
    def __init__(self, id: int, item: Any):
        """
        Args:
            id: int
            item: EntityCarrier[T]
        """
        super().__init__(id=id)
        self._item = item
    
    @property
    def item(self) -> Any:
        return self._item
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, StructureValidationRequest):
            return self.id == other.id
        return False