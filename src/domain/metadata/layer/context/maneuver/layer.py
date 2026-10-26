# src/domain/metadata/unions/context/maneuver/types.py

"""
Module: domain.metadata.unions.context.maneuver.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import Maneuver, ManeuverContextBlueprint, ContextLayer
from transit import ManeuverContextCarrier



class ManeuverContextLayer(ContextLayer[ManeuverContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1.  Catalog of types associated with building and validating
            a Maneuver.

    Attributes:
        model: Type[ManeuverContext]
        carrier: Type[ManeuverContextCarrier]
        blueprint: Type[ManeuverContextBlueprint]

    Provides:

    Super Class:
        ContextTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[ManeuverContext]] | None = None,
            carrier: Optional[Type[ManeuverContextCarrier]] | None = None,
            blueprint: Optional[Type[ManeuverContextBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[ManeuverContext]]
            carrier: Optional[Type[ManeuverContextCarrier]
            blueprint: Optional[Type[ManeuverContextBlueprint] 
        """
        super().__init__(
            model=model or ManeuverContext, 
            carrier=carrier or ManeuverContextCarrier, 
            blueprint=blueprint or ManeuverContextBlueprint
        )
    
    @property
    def model(self) -> Type[ManeuverContext]:
        return cast(Type[ManeuverContext], super().model)
    
    @property
    def carrier(self) -> Type[ManeuverContextCarrier]:
        return cast(Type[ManeuverContextCarrier], super().contextCarrier)
    
    @property
    def blueprint(self) -> Type[ManeuverContextBlueprint]:
        return cast(Type[ManeuverContextBlueprint], super().contextBlueprint)