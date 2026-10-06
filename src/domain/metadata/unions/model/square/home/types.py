# src/domain/metadata/unions/model/square/home/types.py

"""
Module: domain.metadata.unions.square.home.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import HomeSquareBlueprint, HomeSquare, SquareTypeUnion
from transit import HomeSquareCarrier


class HomeSquareTypeUnion(SquareModelTypeUnion[HomeSquare]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a HomeSquare.

    Attributes:
        model: Type[HomeSquare]
        carrier: Type[HomeSquareCarrier]
        blueprint: Type[HomeSquareBlueprint]

    Provides:

    Super Class:
        SquareTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[HomeSquare]] | None = None,
            carrier: Optional[Type[HomeSquareCarrier]] | None = None, 
            blueprint: Optional[Type[HomeSquareBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[HomeSquare]]
            carrier: Optional[Type[HomeSquareCarrier]]
            blueprint: Optional[Type[HomeSquareBlueprint]]
        """
        super().__init__(
            model=model or HomeSquare,
            carrier=carrier or HomeSquareCarrier,
            blueprint=blueprint or HomeSquareBlueprint
        )
    
    @property
    def model(self) -> Type[HomeSquare]:
        return cast(Type[HomeSquare], super().model)
    
    @property
    def carrier(self) -> Type[HomeSquareCarrier]:
        return cast(Type[HomeSquareCarrier], super().reference)
    
    @property
    def blueprint(self) -> Type[HomeSquareBlueprint]:
        return cast(Type[HomeSquareBlueprint], super().blueprint)