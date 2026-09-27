# src/domain/extract/model/rank/extract.py

"""
Module: domain.extract.model.rank.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelPrimeExtract
from domain import Rank, RankBlueprint
from transit import RankCarrier


class RankPrimeExtract(ModelPrimeExtract[Rank]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for RankValidator.

    Attributes:
        carrier: RankCarrier
        blueprint: Optional[RankBlueprint]

    Provides:
        blueprint_exists: bool
        no_blueprint_exists: bool

    Super Class:
        ModelPrimeExtract
    """

    def __init__(
            self,
            carrier: RankCarrier,
            blueprint: Optional[RankBlueprint] | None = None,
    ):
        """
        Args:
            carrier: EntityCarrier[Rank]
            blueprint: Optional[Blueprint[Rank]]
        """
        super().__init__(carrier=carrier, blueprint=blueprint,)
        
    @property
    def carrier(self) -> RankCarrier:
        return cast(RankCarrier, super().carrier)
    
    @property
    def blueprint(self) -> Optional[RankBlueprint]:
        return cast(RankBlueprint,super().blueprint)