# src/domain/metadata/unions/struct/register/square/types.py

"""
Module: domain.metadata.unions.struct.register.square.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import RegisterLayer, SquareRegister, SquareRegisterBlueprint
from transit import StructCarrier

class SquareRegisterLayer(RegisterLayer[SquareRegister]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a SquareRegister.

    Attributes:
        model: Type[SquareRegister]
        blueprint: Type[SquareRegisterBlueprint]
        
    Provides:

    Super Class:
        SquareRegisterTypeUnion
    """
    
    def __init__(
            self,
            model: Optional[Type[SquareRegister]] | None = None,
            blueprint: Optional[Type[SquareRegisterBlueprint]] | None = None,
    ):
        """
        Args:
            model: Type[SquareRegister]
            carrier: Type[StructCarrier[SquareRegister]]
            blueprint: Type[SquareRegisterBlueprint]
        """
        super().__init__(
            model=model or SquareRegister,
            blueprint=blueprint or SquareRegisterBlueprint,
        )
        
    @property
    def model(self) -> Type[SquareRegister]:
        return cast(Type[SquareRegister], super().model)
    
    @property
    def blueprint(self) -> Type[SquareRegisterBlueprint]:
        return cast(Type[SquareRegisterBlueprint], super().model)