# src/domain/metadata/unions/rank/knight/types.py

"""
Module: domain.metadata.unions.rank.knight.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import Knight, KnightBlueprint, RankTypeUnion
from transit import KnightCarrier


class KnightTypeUnion(RankTypeUnion[Knight]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a Knight.

    Attributes:
        model: Type[Knight]
        carrier: Type[KnightCarrier]
        blueprint: Type[KnightBlueprint]

    Provides:

    Super Class:
        RankTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[Knight]] | None = None,
            carrier: Optional[Type[KnightCarrier]] | None = None, 
            blueprint: Optional[Type[KnightBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[Knight]]
            carrier: Optional[Type[KnightCarrier]
            blueprint: Optional[Type[KnightBlueprint] 
        """
        super().__init__(
            model=model or Knight, 
            carrier=carrier or KnightCarrier, 
            blueprint=blueprint or KnightBlueprint
        )
    
    @property
    def model(self) -> Type[Knight]:
        return cast(Type[Knight], super().model)
    
    @property
    def carrier(self) -> Type[KnightCarrier]:
        return cast(Type[KnightCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[KnightBlueprint]:
        return cast(Type[KnightBlueprint], super().blueprint)