# src/domain/metadata/unions/rank/king/types.py

"""
Module: domain.metadata.unions.rank.king.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import King, KingBlueprint, RankTypeUnion
from transit import KingCarrier


class KingTypeUnion(RankTypeUnion[King]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a King.

    Attributes:
        model: Type[King]
        carrier: Type[KingCarrier]
        blueprint: Type[KingBlueprint]

    Provides:

    Super Class:
        RankTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[King]] | None = None,
            carrier: Optional[Type[KingCarrier]] | None = None, 
            blueprint: Optional[Type[KingBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[King]]
            carrier: Optional[Type[KingCarrier]
            blueprint: Optional[Type[KingBlueprint] 
        """
        super().__init__(
            model=model or King, 
            carrier=carrier or KingCarrier, 
            blueprint=blueprint or KingBlueprint
        )
    
    @property
    def model(self) -> Type[King]:
        return cast(Type[King], super().model)
    
    @property
    def carrier(self) -> Type[KingCarrier]:
        return cast(Type[KingCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[KingBlueprint]:
        return cast(Type[KingBlueprint], super().blueprint)