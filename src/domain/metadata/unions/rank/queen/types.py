# src/domain/metadata/unions/rank/queen/types.py

"""
Module: domain.metadata.unions.rank.queen.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import Queen, QueenBlueprint, RankTypeUnion
from transit import QueenCarrier


class QueenTypeUnion(RankTypeUnion[Queen]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a Queen.

    Attributes:
        model: Type[Queen]
        carrier: Type[QueenCarrier]
        blueprint: Type[QueenBlueprint]

    Provides:

    Super Class:
        RankTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[Queen]] | None = None,
            carrier: Optional[Type[QueenCarrier]] | None = None, 
            blueprint: Optional[Type[QueenBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[Queen]]
            carrier: Optional[Type[QueenCarrier]
            blueprint: Optional[Type[QueenBlueprint] 
        """
        super().__init__(
            model=model or Queen, 
            carrier=carrier or QueenCarrier, 
            blueprint=blueprint or QueenBlueprint
        )
    
    @property
    def model(self) -> Type[Queen]:
        return cast(Type[Queen], super().model)
    
    @property
    def carrier(self) -> Type[QueenCarrier]:
        return cast(Type[QueenCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[QueenBlueprint]:
        return cast(Type[QueenBlueprint], super().blueprint)