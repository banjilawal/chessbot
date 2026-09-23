# src/domain/metadata/unions/strcture/register/identity/manifest.py

"""
Module: domain.metadata.unions.structure.register.identity.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import RegisterTypeUnion, IdentityRegister, IdentityRegisterBlueprint
from transit import EntityCarrier

class IdentityRegisterTypeUnion(RegisterTypeUnion[IdentityRegister]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a IdentityRegister.

    Attributes:
        model: Type[IdentityRegister]
        carrier: Type[EntityCarrier[IdentityRegister]]
        blueprint: Type[IdentityRegisterBlueprint]
        
    Provides:

    Super Class:
        IdentityRegisterTypeUnion
    """
    
    def __init__(
            self,
            carrier: Type[EntityCarrier[IdentityRegister]],
            model: Optional[Type[IdentityRegister]] | None = None,
            blueprint: Optional[Type[IdentityRegisterBlueprint]] | None = None,
    ):
        """
        Args:
            model: Type[IdentityRegister]
            carrier: Type[EntityCarrier[IdentityRegister]]
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
    def carrier(self) -> Type[EntityCarrier[IdentityRegister]]:
        return cast(Type[EntityCarrier[IdentityRegister]], super().carrier)
    
    @property
    def blueprint(self) -> Type[IdentityRegisterBlueprint]:
        return cast(Type[IdentityRegisterBlueprint], super().model)