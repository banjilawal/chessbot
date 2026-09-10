# src/domain/exchange/request/validation/model/path/request.py

"""
Module: domain.exchange.request.validation.model.path.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import ModelValidationRequest, Path
from transit import PathCarrier


class PathValidationRequest(ModelValidationRequest[Path]):
    """
     Role:
         - Messaging
         - Transport

     Responsibilities:
        1. Send job details to a PathValidator.

     Attributes:
         id: int
         item: PathCarrier

     Provides:
     
     Super Class:
        ModelValidationRequest
     """
    
    def __init__(self, id: int, item: PathCarrier):
        """
        Args:
            id: int
            item: PathCarrier
        """
        super().__init__(id=id, item=item)

    @property
    def item(self) -> PathCarrier:
        return cast(PathCarrier, super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, PathValidationRequest):
            return self.id == other.id
        return False