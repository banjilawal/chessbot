# src/domain/metadata/unions/model/maneuver/types.py

"""
Module: domain.metadata.unions.maneuver.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import Maneuver, ManeuverBlueprint, ModelTypeUnion
from transit import ManeuverCarrier



class ManeuverTypeUnion(ModelTypeUnion[Maneuver]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a Maneuver.

    Attributes:
        model: Type[Maneuver]
        carrier: Type[ManeuverCarrier]
        blueprint: Type[ManeuverBlueprint]

    Provides:

    Super Class:
        ModelTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[Maneuver]] | None = None,
            carrier: Optional[Type[ManeuverCarrier]] | None = None, 
            blueprint: Optional[Type[ManeuverBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[Maneuver]]
            carrier: Optional[Type[ManeuverCarrier]
            blueprint: Optional[Type[ManeuverBlueprint] 
        """
        super().__init__(
            model=model or Maneuver, 
            carrier=carrier or ManeuverCarrier, 
            blueprint=blueprint or ManeuverBlueprint
        )
    
    @property
    def model(self) -> Type[Maneuver]:
        return cast(Type[Maneuver], super().model)
    
    @property
    def carrier(self) -> Type[ManeuverCarrier]:
        return cast(Type[ManeuverCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[ManeuverBlueprint]:
        return cast(Type[ManeuverBlueprint], super().blueprint)