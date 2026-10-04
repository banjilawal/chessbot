# src/domain/metadata/unions/strcture/register/cartesian/manifest.py

"""
Module: domain.metadata.unions.struct.register.cartesian.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import RegisterTypeUnion
from transit import EntityCarrier

class CartesianToggleRegisterTypeUnion(RegisterTypeUnion[CartesianToggleRegister]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a CartesianToggleRegister.

    Attributes:
        model: Type[CartesianRegister]
        carrier: Type[EntityCarrier[CartesianRegister]]
        blueprint: Type[CartesianRegisterBlueprint]
        
    Provides:

    Super Class:
        CartesianRegisterTypeUnion
    """
    
    def __init__(
            self,
            carrier: Type[EntityCarrier[CartesianRegister]],
            model: Optional[Type[CartesianRegister]] | None = None,
            blueprint: Optional[Type[CartesianRegisterBlueprint]] | None = None,
    ):
        """
        Args:
            model: Type[CartesianRegister]
            carrier: Type[EntityCarrier[CartesianRegister]]
            blueprint: Type[CartesianRegisterBlueprint]
        """
        super().__init__(
            model=model or CartesianRegister,
            blueprint=blueprint or CartesianRegisterBlueprint,
            carrier=carrier,
        )
        
    @property
    def model(self) -> Type[CartesianRegister]:
        return cast(Type[CartesianRegister], super().model)
    
    @property
    def carrier(self) -> Type[EntityCarrier[CartesianRegister]]:
        return cast(Type[EntityCarrier[CartesianRegister]], super().carrier)
    
    @property
    def blueprint(self) -> Type[CartesianRegisterBlueprint]:
        return cast(Type[CartesianRegisterBlueprint], super().model)