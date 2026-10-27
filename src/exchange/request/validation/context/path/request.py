# src/exchange/request/validation/context/path/request.py

"""
Module: exchange.request.validation.context.path.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from exchange import ContextValidationRequest, Path
from transit import PathContextCarrier


class PathContextValidationRequest(ContextValidationRequest[PathContext]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1. Provide a PathContextValidator job details.

     Attributes:
         id: int
         item: PathContextCarrier

     Provides:
     
     Super Class:
        ContextValidationRequest
     """
    
    def __init__(self, id: int, item: PathContextCarrier):
        """
        Args:
            id: int
            item: PathContextCarrier
        """
        super().__init__(id=id, item=item)

    @property
    def item(self) -> PathContextCarrier:
        return cast(PathContextCarrier, super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, PathContextValidationRequest):
            return self.id == other.id
        return False