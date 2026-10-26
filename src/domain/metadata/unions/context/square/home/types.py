# src/domain/metadata/unions/context/square/home/types.py

"""
Module: domain.metadata.unions.context.square.home.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import HomeSquareContextBlueprint, HomeSquare, SquareContextTypeUnion
from transit import HomeSquareContextCarrier


class HomeSquareContextTypeUnion(SquareContextTypeUnion[HomeSquareContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a HomeSquare.

    Attributes:
        model: Type[HomeSquareContext]
        carrier: Type[HomeSquareContextCarrier]
        blueprint: Type[HomeSquareContextBlueprint]

    Provides:

    Super Class:
        SquareContextTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[HomeSquareContext]] | None = None,
            carrier: Optional[Type[HomeSquareContextCarrier]] | None = None,
            blueprint: Optional[Type[HomeSquareContextBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[HomeSquareContext]]
            carrier: Optional[Type[HomeSquareContextCarrier]]
            blueprint: Optional[Type[HomeSquareContextBlueprint]]
        """
        super().__init__(
            model=model or HomeSquareContext, 
            carrier=carrier or HomeSquareContextCarrier,
            blueprint=blueprint or HomeSquareContextBlueprint
        )
    
    @property
    def model(self) -> Type[HomeSquareContext]:
        return cast(Type[HomeSquareContext], super().model)
    
    @property
    def carrier(self) -> Type[HomeSquareContextCarrier]:
        return cast(Type[HomeSquareContextCarrier], super().reference)
    
    @property
    def blueprint(self) -> Type[HomeSquareContextBlueprint]:
        return cast(Type[HomeSquareContextBlueprint], super().contextBlueprint)