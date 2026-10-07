# src/domain/metadata/unions/strcture/model/footstep/manifest.py

"""
Module: domain.metadata.unions.model.footstep.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import ModelTypeUnion, Footstep, FootstepBlueprint
from transit import FootstepCarrier


class FootstepTypeUnion(ModelTypeUnion[Footstep]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a Footstep.

    Attributes:
        model: Type[Footstep]
        carrier: Type[FootstepCarrier]
        blueprint: Type[FootstepBlueprint]
        
    Provides:

    Super Class:
        FootstepTypeUnion
    """
    
    def __init__(
            self,
            model: Optional[Type[Footstep]] | None = None,
            carrier: Optional[Type[FootstepCarrier]] | None = None,
            blueprint: Optional[Type[FootstepBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[Footstep]]
            carrier: Optional[Type[FootstepCarrier]]
            blueprint: Optional[Type[FootstepBlueprint]]
        """
        super().__init__(
            model=model or Footstep,
            carrier=carrier or FootstepCarrier,
            blueprint=blueprint or FootstepBlueprint,
        )
        
    @property
    def model(self) -> Type[Footstep]:
        return cast(Type[Footstep], super().model)
    
    @property
    def carrier(self) -> Type[FootstepCarrier]:
        return cast(Type[FootstepCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[FootstepBlueprint]:
        return cast(Type[FootstepBlueprint], super().model)