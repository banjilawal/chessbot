# src/domain/metadata/unions/context/board/types.py

"""
Module: domain.metadata.unions.context.board.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import Board, BoardContextBlueprint, ContextLayer
from transit import BoardContextCarrier


class BoardContextLayer(ContextLayer[BoardContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating an Board.

    Attributes:
        model: Type[BoardContext]
        carrier: Type[BoardContextCarrier]
        blueprint: Type[BoardContextBlueprint]

    Provides:

    Super Class:
        ContextTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[BoardContext]] | None = None,
            carrier: Optional[Type[BoardContextCarrier]] | None = None,
            blueprint: Optional[Type[BoardContextBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[BoardContext]]
            carrier: Optional[Type[BoardContextCarrier]
            blueprint: Optional[Type[BoardContextBlueprint] 
        """
        super().__init__(
            model=model or BoardContext, 
            carrier=carrier or BoardContextCarrier, 
            blueprint=blueprint or BoardContextBlueprint
        )
    
    @property
    def model(self) -> Type[BoardContext]:
        return cast(Type[BoardContext], super().model)
    
    @property
    def carrier(self) -> Type[BoardContextCarrier]:
        return cast(Type[BoardContextCarrier], super().contextCarrier)
    
    @property
    def blueprint(self) -> Type[BoardContextBlueprint]:
        return cast(Type[BoardContextBlueprint], super().contextBlueprint)