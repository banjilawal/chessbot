# src/exchange/request/fabrication/model/scalar/request.py

"""
Module: exchange.request.fabrication.model.scalar.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from exchange import ModelBuildRequest
from domain import Scalar
from transit import ScalarCarrier


class ScalarBuildRequest(ModelBuildRequest[Scalar]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1. Provide details about a Scalar a build job.

     Attributes:
         id: int
         item: ScalarCarrier

     Provides:
     
     Super Class:
        ModelBuildRequest
     """
    
    def __init__(self, id: int, item: ScalarCarrier):
        """
        Args:
            id: int
            item: ScalarCarrier
        """
        super().__init__(id=id, item=item)

    @property
    def item(self) -> ScalarCarrier:
        return cast(ScalarCarrier, super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ScalarBuildRequest):
            return self.id == other.id
        return False