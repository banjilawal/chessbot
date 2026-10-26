# src/domain/metadata/unions/context/square/types.py

"""
Module: domain.metadata.unions.context.square.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import ContextLayer, Square, SquareContextBlueprint
from transit import SquareContextCarrier


class SquareContextLayer(ContextLayer[SquareContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a Square.

    Attributes:
        model: Type[SquareContext]
        carrier: Type[SquareContextCarrier]
        blueprint: Type[SquareContextBlueprint]
        
    Provides:

    Super Class:
        ContextTypeUnion
    """
    
    def __init__(
            self,
            model: Optional[Type[SquareContext]] | None = None,
            carrier: Optional[Type[SquareContextCarrier]] | None = None,
            blueprint: Optional[Type[SquareContextBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[SquareContext]]
            carrier: Optional[Type[SquareContextCarrier]]
            blueprint: Optional[Type[SquareContextBlueprint]]
        """
        super().__init__(
            model=model or SquareContext, 
            carrier=carrier or Type[SquareContextCarrier],
            blueprint=blueprint or SquareContextBlueprint,
        )
    
    @property
    def model(self) -> Type[SquareContext]:
        return cast(Type[SquareContext], super().model)
    
    @property
    def carrier(self) -> Type[SquareContextCarrier]:
        return cast(Type[SquareContextCarrier], super().contextCarrier)
    
    @property
    def blueprint(self) -> Type[SquareContextBlueprint]:
        return cast(Type[SquareContextBlueprint], super().contextBlueprint)