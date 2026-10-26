# src/domain/extract/context/maneuver/extract.py

"""
Module: domain.extract.context.maneuver.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Maneuver, ManeuverContextBlueprint, ContextPrimeExtract
from transit import ManeuverContextCarrier


class ManeuverContextPrimeExtract(ContextPrimeExtract[ManeuverContext]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist ContextBlueprint and ContextCarrier data for ManeuverValidator.

    Attributes:
        contextCarrier: ManeuverContextCarrier
        blueprint: Optional[ManeuverContextBlueprint]

    Provides:

    Super Class:
        ContextPrimeExtract
    """

    def __init__(
            self,
            reference: ManeuverContextCarrier,
            blueprint: Optional[ManeuverContextBlueprint] | None = None,
    ):
        """
        Args:
            reference: ManeuverContextCarrier
            blueprint: Optional[ContextBlueprint[Maneuver]]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> ManeuverContextCarrier:
        return cast(ManeuverContextCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[ManeuverContextBlueprint]:
        return cast(ManeuverContextBlueprint, super().blueprint)