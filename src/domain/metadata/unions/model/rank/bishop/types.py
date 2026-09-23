# src/domain/metadata/unions/rank/bishop/types.py

"""
Module: domain.metadata.unions.rank.bishop.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import Bishop, BishopBlueprint, RankTypeUnion
from transit import BishopCarrier


class BishopTypeUnion(RankTypeUnion[Bishop]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a Bishop.

    Attributes:
        model: Type[Bishop]
        carrier: Type[BishopCarrier]
        blueprint: Type[BishopBlueprint]

    Provides:

    Super Class:
        RankTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[Bishop]] | None = None,
            carrier: Optional[Type[BishopCarrier]] | None = None, 
            blueprint: Optional[Type[BishopBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[Bishop]]
            carrier: Optional[Type[BishopCarrier]
            blueprint: Optional[Type[BishopBlueprint] 
        """
        super().__init__(
            model=model or Bishop, 
            carrier=carrier or BishopCarrier, 
            blueprint=blueprint or BishopBlueprint
        )
    
    @property
    def model(self) -> Type[Bishop]:
        return cast(Type[Bishop], super().model)
    
    @property
    def carrier(self) -> Type[BishopCarrier]:
        return cast(Type[BishopCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[BishopBlueprint]:
        return cast(Type[BishopBlueprint], super().blueprint)