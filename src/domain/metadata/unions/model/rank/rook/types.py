# src/domain/metadata/unions/rank/rook/types.py

"""
Module: domain.metadata.unions.rank.rook.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import Rook, RookBlueprint, RankTypeUnion
from transit import RookCarrier


class RookTypeUnion(RankTypeUnion[Rook]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a Rook.

    Attributes:
        model: Type[Rook]
        carrier: Type[RookCarrier]
        blueprint: Type[RookBlueprint]

    Provides:

    Super Class:
        RankTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[Rook]] | None = None,
            carrier: Optional[Type[RookCarrier]] | None = None, 
            blueprint: Optional[Type[RookBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[Rook]]
            carrier: Optional[Type[RookCarrier]
            blueprint: Optional[Type[RookBlueprint] 
        """
        super().__init__(
            model=model or Rook, 
            carrier=carrier or RookCarrier, 
            blueprint=blueprint or RookBlueprint
        )
    
    @property
    def model(self) -> Type[Rook]:
        return cast(Type[Rook], super().model)
    
    @property
    def carrier(self) -> Type[RookCarrier]:
        return cast(Type[RookCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[RookBlueprint]:
        return cast(Type[RookBlueprint], super().blueprint)