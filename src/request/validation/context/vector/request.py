# src/request/validation/context/vector/request.py

"""
Module: request.validation.context.vector.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import VectorContext
from request import ContextValidationRequest
from transit import VectorContextCarrier


class VectorContextValidationRequest(ContextValidationRequest[VectorContext]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide details about an VectorContextValidation job.

     Attributes:
         id: int
         item: VectorContextCarrier

     Provides:
     
     Super Class:
        ContextValidationRequest
     """
    
    def __init__(self, id: int, item: VectorContextCarrier):
        """
        Args:
            id: int
            item: VectorContextCarrier
        """
        super().__init__(id=id, item=item)

    @property
    def item(self) -> VectorContextCarrier:
        return cast(VectorContextCarrier, super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, VectorContextValidationRequest):
            return self.id == other.id
        return False