# src/domain/metadata/unions/strcture/register/vector/manifest.py

"""
Module: domain.metadata.unions.struct.register.vector.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import RegisterTypeUnion, VectorRegister, VectorRegisterBlueprint
from transit import EntityCarrier

class VectorRegisterTypeUnion(RegisterTypeUnion[VectorRegister]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a VectorRegister.

    Attributes:
        model: Type[VectorRegister]
        carrier: Type[EntityCarrier[VectorRegister]]
        blueprint: Type[VectorRegisterBlueprint]
        
    Provides:

    Super Class:
        VectorRegisterTypeUnion
    """
    
    def __init__(
            self,
            carrier: Type[EntityCarrier[VectorRegister]],
            model: Optional[Type[VectorRegister]] | None = None,
            blueprint: Optional[Type[VectorRegisterBlueprint]] | None = None,
    ):
        """
        Args:
            model: Type[VectorRegister]
            carrier: Type[EntityCarrier[VectorRegister]]
            blueprint: Type[VectorRegisterBlueprint]
        """
        super().__init__(
            model=model or VectorRegister,
            blueprint=blueprint or VectorRegisterBlueprint,
            carrier=carrier,
        )
        
    @property
    def model(self) -> Type[VectorRegister]:
        return cast(Type[VectorRegister], super().model)
    
    @property
    def carrier(self) -> Type[EntityCarrier[VectorRegister]]:
        return cast(Type[EntityCarrier[VectorRegister]], super().carrier)
    
    @property
    def blueprint(self) -> Type[VectorRegisterBlueprint]:
        return cast(Type[VectorRegisterBlueprint], super().model)