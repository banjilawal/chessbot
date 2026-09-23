# src/domain/metadata/unions/strcture/register/coord/manifest.py

"""
Module: domain.metadata.unions.structure.register.coord.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import RegisterTypeUnion, CoordRegister, CoordRegisterBlueprint
from transit import EntityCarrier

class CoordRegisterTypeUnion(RegisterTypeUnion[CoordRegister]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a CoordRegister.

    Attributes:
        model: Type[CoordRegister]
        carrier: Type[EntityCarrier[CoordRegister]]
        blueprint: Type[CoordRegisterBlueprint]
        
    Provides:

    Super Class:
        CoordRegisterTypeUnion
    """
    
    def __init__(
            self,
            carrier: Type[EntityCarrier[CoordRegister]],
            model: Optional[Type[CoordRegister]] | None = None,
            blueprint: Optional[Type[CoordRegisterBlueprint]] | None = None,
    ):
        """
        Args:
            model: Type[CoordRegister]
            carrier: Type[EntityCarrier[CoordRegister]]
            blueprint: Type[CoordRegisterBlueprint]
        """
        super().__init__(
            model=model or CoordRegister,
            blueprint=blueprint or CoordRegisterBlueprint,
            carrier=carrier,
        )
        
    @property
    def model(self) -> Type[CoordRegister]:
        return cast(Type[CoordRegister], super().model)
    
    @property
    def carrier(self) -> Type[EntityCarrier[CoordRegister]]:
        return cast(Type[EntityCarrier[CoordRegister]], super().carrier)
    
    @property
    def blueprint(self) -> Type[CoordRegisterBlueprint]:
        return cast(Type[CoordRegisterBlueprint], super().model)