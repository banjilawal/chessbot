# src/domain/metadata/unions/square/types.py

"""
Module: domain.metadata.unions.square.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import Square, SquareBlueprint, TypeUnion
from transit import SquareCarrier


class SquareTypeUnion(TypeUnion[Square]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating an Square.

    Attributes:
        model: Type[Square]
        carrier: Type[SquareCarrier]
        blueprint: Type[SquareBlueprint]

    Provides:

    Super Class:
        TypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[Square]] | None = None,
            carrier: Optional[Type[SquareCarrier]] | None = None, 
            blueprint: Optional[Type[SquareBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[Square]]
            carrier: Optional[Type[SquareCarrier]
            blueprint: Optional[Type[SquareBlueprint] 
        """
        super().__init__(
            model=model or Square, 
            carrier=carrier or SquareCarrier, 
            blueprint=blueprint or SquareBlueprint
        )
    
    @property
    def model(self) -> Type[Square]:
        return cast(Type[Square], super().model)
    
    @property
    def carrier(self) -> Type[SquareCarrier]:
        return cast(Type[SquareCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[SquareBlueprint]:
        return cast(Type[SquareBlueprint], super().blueprint)