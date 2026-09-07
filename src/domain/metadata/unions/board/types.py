# src/domain/metadata/unions/board/types.py

"""
Module: domain.metadata.unions.board.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import Board, BoardBlueprint, TypeUnion
from transit import BoardCarrier


class BoardTypeUnion(TypeUnion[Board]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating an Board.

    Attributes:
        model: Type[Board]
        carrier: Type[BoardCarrier]
        blueprint: Type[BoardBlueprint]

    Provides:

    Super Class:
        TypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[Board]] | None = None,
            carrier: Optional[Type[BoardCarrier]] | None = None, 
            blueprint: Optional[Type[BoardBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[Board]]
            carrier: Optional[Type[BoardCarrier]
            blueprint: Optional[Type[BoardBlueprint] 
        """
        super().__init__(
            model=model or Board, 
            carrier=carrier or BoardCarrier, 
            blueprint=blueprint or BoardBlueprint
        )
    
    @property
    def model(self) -> Type[Board]:
        return cast(Type[Board], super().model)
    
    @property
    def carrier(self) -> Type[BoardCarrier]:
        return cast(Type[BoardCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[BoardBlueprint]:
        return cast(Type[BoardBlueprint], super().blueprint)