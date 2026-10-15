# src/domain/metadata/unions/struct/register/identity/types.py

"""
Module: domain.metadata.unions.struct.register.identity.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import RegisterTypeUnion, IdentityRegister, IdentityRegisterBlueprint
from transit import StructCarrier

class IdentityRegisterTypeUnion(RegisterTypeUnion[IdentityRegister]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a IdentityRegister.

    Attributes:
        model: Type[IdentityRegister]
        carrier: Type[StructCarrier[IdentityRegister]]
        blueprint: Type[IdentityRegisterBlueprint]
        
    Provides:

    Super Class:
        IdentityRegisterTypeUnion
    """
    
    def __init__(
            self,
            carrier: Type[StructCarrier[IdentityRegister]],
            model: Optional[Type[IdentityRegister]] | None = None,
            blueprint: Optional[Type[IdentityRegisterBlueprint]] | None = None,
    ):
        """
        Args:
            model: Type[IdentityRegister]
            carrier: Type[StructCarrier[IdentityRegister]]
            blueprint: Type[IdentityRegisterBlueprint]
        """
        super().__init__(
            model=model or IdentityRegister,
            blueprint=blueprint or IdentityRegisterBlueprint,
            carrier=carrier,
        )
        
    @property
    def model(self) -> Type[IdentityRegister]:
        return cast(Type[IdentityRegister], super().model)
    
    @property
    def carrier(self) -> Type[StructCarrier[IdentityRegister]]:
        return cast(Type[StructCarrier[IdentityRegister]], super().carrier)
    
    @property
    def blueprint(self) -> Type[IdentityRegisterBlueprint]:
        return cast(Type[IdentityRegisterBlueprint], super().model)