# src/exchange/request/fabrication/model/rank/request.py

"""
Module: exchange.request.fabrication.model.rank.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from exchange import ModelBuildRequest
from domain import Rank
from transit import RankCarrier


class RankBuildRequest(ModelBuildRequest[Rank]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1. Provide details about a Rank a build job.

     Attributes:
         id: int
         item: RankCarrier

     Provides:
     
     Super Class:
        ModelBuildRequest
     """
    
    def __init__(self, id: int, item: RankCarrier):
        """
        Args:
            id: int
            item: RankCarrier
        """
        super().__init__(id=id, item=item)

    @property
    def item(self) -> RankCarrier:
        return cast(RankCarrier, super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, RankBuildRequest):
            return self.id == other.id
        return False