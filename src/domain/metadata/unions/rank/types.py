# src/domain/metadata/unions/rank/types.py

"""
Module: domain.metadata.unions.rank.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import Rank, RankBlueprint, TypeUnion
from transit import RankCarrier


class RankTypeUnion(TypeUnion[Rank]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating an Rank.

    Attributes:
        model: Type[Rank]
        carrier: Type[RankCarrier]
        blueprint: Type[RankBlueprint]

    Provides:

    Super Class:
        TypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[Rank]] | None = None,
            carrier: Optional[Type[RankCarrier]] | None = None, 
            blueprint: Optional[Type[RankBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[Rank]]
            carrier: Optional[Type[RankCarrier]
            blueprint: Optional[Type[RankBlueprint] 
        """
        super().__init__(
            model=model or Rank, 
            carrier=carrier or RankCarrier, 
            blueprint=blueprint or RankBlueprint
        )
    
    @property
    def model(self) -> Type[Rank]:
        return cast(Type[Rank], super().model)
    
    @property
    def carrier(self) -> Type[RankCarrier]:
        return cast(Type[RankCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[RankBlueprint]:
        return cast(Type[RankBlueprint], super().blueprint)