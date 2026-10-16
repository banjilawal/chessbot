# src/exchange/request/fabrication/model/square/request.py

"""
Module: exchange.request.fabrication.model.square.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from exchange import ModelBuildRequest
from domain import Square
from transit import SquareCarrier


class SquareBuildRequest(ModelBuildRequest[Square]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1. Provide details about a Square a build job.

     Attributes:
         id: int
         item: SquareCarrier

     Provides:
     
     Super Class:
        ModelBuildRequest
     """
    
    def __init__(self, id: int, item: SquareCarrier):
        """
        Args:
            id: int
            item: SquareCarrier
        """
        super().__init__(id=id, item=item)

    @property
    def item(self) -> SquareCarrier:
        return cast(SquareCarrier, super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, SquareBuildRequest):
            return self.id == other.id
        return False