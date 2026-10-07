# src/domain/metadata/unions/strcture/chart/footstep/manifest.py

"""
Module: domain.metadata.unions.struct.chart.footstep.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import ChartTypeUnion, Footstep, FootstepBlueprint
from transit import EntityCarrier

class FootstepTypeUnion(ChartTypeUnion[Footstep]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a Footstep.

    Attributes:
        model: Type[Footstep]
        carrier: Type[EntityCarrier[Footstep]]
        blueprint: Type[FootstepBlueprint]
        
    Provides:

    Super Class:
        FootstepTypeUnion
    """
    
    def __init__(
            self,
            carrier: Type[EntityCarrier[Footstep]],
            model: Optional[Type[Footstep]] | None = None,
            blueprint: Optional[Type[FootstepBlueprint]] | None = None,
    ):
        """
        Args:
            model: Type[Footstep]
            carrier: Type[EntityCarrier[Footstep]]
            blueprint: Type[FootstepBlueprint]
        """
        super().__init__(
            model=model or Footstep,
            blueprint=blueprint or FootstepBlueprint,
            carrier=carrier,
        )
        
    @property
    def model(self) -> Type[Footstep]:
        return cast(Type[Footstep], super().model)
    
    @property
    def carrier(self) -> Type[EntityCarrier[Footstep]]:
        return cast(Type[EntityCarrier[Footstep]], super().carrier)
    
    @property
    def blueprint(self) -> Type[FootstepBlueprint]:
        return cast(Type[FootstepBlueprint], super().model)