# src/request/validation/context/coord/request.py

"""
Module: request.validation.context.coord.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import CoordContext
from request import ContextValidationRequest
from transit import CoordContextCarrier


class CoordContextValidationRequest(ContextValidationRequest[CoordContext]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide details about an CoordContextValidation job.

     Attributes:
         id: int
         item: CoordContextCarrier

     Provides:
     
     Super Class:
        ContextValidationRequest
     """
    
    def __init__(self, id: int, item: CoordContextCarrier):
        """
        Args:
            id: int
            item: CoordContextCarrier
        """
        super().__init__(id=id, item=item)

    @property
    def item(self) -> CoordContextCarrier:
        return cast(CoordContextCarrier, super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, CoordContextValidationRequest):
            return self.id == other.id
        return False