# src/domain/extract/struct/maneuver/extract.py

"""
Module: domain.extract.struct.maneuver.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Maneuver, ManeuverBlueprint, StructPrimeExtract
from transit import ManeuverCarrier


class ManeuverPrimeExtract(StructPrimeExtract[Maneuver]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for ManeuverValidator.

    Attributes:
        carrier: ManeuverCarrier
        blueprint: Optional[ManeuverBlueprint]

    Provides:

    Super Class:
        StructPrimeExtract
    """

    def __init__(
            self,
            carrier: ManeuverCarrier,
            blueprint: Optional[ManeuverBlueprint] | None = None,
    ):
        """
        Args:
            carrier: ManeuverCarrier
            blueprint: Optional[Blueprint[Maneuver]]
        """
        super().__init__(carrier=carrier, blueprint=blueprint)
        
    @property
    def carrier(self) -> ManeuverCarrier:
        return cast(ManeuverCarrier, super().carrier)
    
    @property
    def blueprint(self) -> Optional[ManeuverBlueprint]:
        return cast(ManeuverBlueprint, super().blueprint)