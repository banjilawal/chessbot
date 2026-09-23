# src/domain/metadata/unions/rank/pawn/types.py

"""
Module: domain.metadata.unions.rank.pawn.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import Pawn, PawnBlueprint, RankTypeUnion
from transit import PawnCarrier


class PawnTypeUnion(RankTypeUnion[Pawn]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a Pawn.

    Attributes:
        model: Type[Pawn]
        carrier: Type[PawnCarrier]
        blueprint: Type[PawnBlueprint]

    Provides:

    Super Class:
        RankTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[Pawn]] | None = None,
            carrier: Optional[Type[PawnCarrier]] | None = None, 
            blueprint: Optional[Type[PawnBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[Pawn]]
            carrier: Optional[Type[PawnCarrier]
            blueprint: Optional[Type[PawnBlueprint] 
        """
        super().__init__(
            model=model or Pawn, 
            carrier=carrier or PawnCarrier, 
            blueprint=blueprint or PawnBlueprint
        )
    
    @property
    def model(self) -> Type[Pawn]:
        return cast(Type[Pawn], super().model)
    
    @property
    def carrier(self) -> Type[PawnCarrier]:
        return cast(Type[PawnCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[PawnBlueprint]:
        return cast(Type[PawnBlueprint], super().blueprint)