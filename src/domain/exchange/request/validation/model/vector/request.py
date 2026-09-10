# src/domain/exchange/request/validation/model/vector/request.py

"""
Module: domain.exchange.request.validation.model.vector.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import ModelValidationRequest, Vector
from transit import VectorCarrier


class VectorValidationRequest(ModelValidationRequest[Vector]):
    """
     Role:
         - Messaging
         - Transport

     Responsibilities:
        1. Send job details to a VectorValidator.

     Attributes:
         id: int
         item: VectorCarrier

     Provides:
     
     Super Class:
        ModelValidationRequest
     """
    
    def __init__(self, id: int, item: VectorCarrier):
        """
        Args:
            id: int
            item: VectorCarrier
        """
        super().__init__(id=id, item=item)

    @property
    def item(self) -> VectorCarrier:
        return cast(VectorCarrier, super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ModelValidationRequest):
            return self.id == other.id
        return False