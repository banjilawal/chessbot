# src/domain/metadata/unions/strcture/chart/participate/manifest.py

"""
Module: domain.metadata.unions.struct.chart.participate.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import ChartTypeUnion, Participation, ParticipationBlueprint
from transit import EntityCarrier

class ParticipationTypeUnion(ChartTypeUnion[Participation]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a Participation.

    Attributes:
        model: Type[Participation]
        carrier: Type[EntityCarrier[Participation]]
        blueprint: Type[ParticipationBlueprint]
        
    Provides:

    Super Class:
        ParticipationTypeUnion
    """
    
    def __init__(
            self,
            carrier: Type[EntityCarrier[Participation]],
            model: Optional[Type[Participation]] | None = None,
            blueprint: Optional[Type[ParticipationBlueprint]] | None = None,
    ):
        """
        Args:
            model: Type[Participation]
            carrier: Type[EntityCarrier[Participation]]
            blueprint: Type[ParticipationBlueprint]
        """
        super().__init__(
            model=model or Participation,
            blueprint=blueprint or ParticipationBlueprint,
            carrier=carrier,
        )
        
    @property
    def model(self) -> Type[Participation]:
        return cast(Type[Participation], super().model)
    
    @property
    def carrier(self) -> Type[EntityCarrier[Participation]]:
        return cast(Type[EntityCarrier[Participation]], super().carrier)
    
    @property
    def blueprint(self) -> Type[ParticipationBlueprint]:
        return cast(Type[ParticipationBlueprint], super().model)