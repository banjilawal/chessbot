# src/domain/metadata/unions/strcture/chart/walk/manifest.py

"""
Module: domain.metadata.unions.struct.chart.walk.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import ChartTypeUnion, Walk, WalkBlueprint
from transit import EntityCarrier

class WalkTypeUnion(ChartTypeUnion[Walk]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a Walk.

    Attributes:
        model: Type[Walk]
        carrier: Type[EntityCarrier[Walk]]
        blueprint: Type[WalkBlueprint]
        
    Provides:

    Super Class:
        WalkTypeUnion
    """
    
    def __init__(
            self,
            carrier: Type[EntityCarrier[Walk]],
            model: Optional[Type[Walk]] | None = None,
            blueprint: Optional[Type[WalkBlueprint]] | None = None,
    ):
        """
        Args:
            model: Type[Walk]
            carrier: Type[EntityCarrier[Walk]]
            blueprint: Type[WalkBlueprint]
        """
        super().__init__(
            model=model or Walk,
            blueprint=blueprint or WalkBlueprint,
            carrier=carrier,
        )
        
    @property
    def model(self) -> Type[Walk]:
        return cast(Type[Walk], super().model)
    
    @property
    def carrier(self) -> Type[EntityCarrier[Walk]]:
        return cast(Type[EntityCarrier[Walk]], super().carrier)
    
    @property
    def blueprint(self) -> Type[WalkBlueprint]:
        return cast(Type[WalkBlueprint], super().model)