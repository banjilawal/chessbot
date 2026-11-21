# src/request/validation/context/square/request.py

"""
Module: request.validation.context.square.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import SquareContext
from request import ContextValidationRequest
from transit import SquareContextCarrier


class SquareContextValidationRequest(ContextValidationRequest[SquareContext]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide details about an SquareContextValidation job.

     Attributes:
         id: int
         item: SquareContextCarrier

     Provides:
     
     Super Class:
        ContextValidationRequest
     """
    
    def __init__(self, id: int, item: SquareContextCarrier):
        """
        Args:
            id: int
            item: SquareContextCarrier
        """
        super().__init__(id=id, item=item)

    @property
    def item(self) -> SquareContextCarrier:
        return cast(SquareContextCarrier, super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, SquareContextValidationRequest):
            return self.id == other.id
        return False