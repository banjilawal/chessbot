# src/domain/extract/model/maneuver/extract.py

"""
Module: domain.extract.model.maneuver.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Maneuver, ManeuverBlueprint, ModelPrimeExtract
from transit import ManeuverCarrier


class ManeuverPrimeExtract(ModelPrimeExtract[Maneuver]):
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
        ModelPrimeExtract
    """

    def __init__(
            self,
            reference: ManeuverCarrier,
            blueprint: Optional[ManeuverBlueprint] | None = None,
    ):
        """
        Args:
            reference: ManeuverCarrier
            blueprint: Optional[Blueprint[Maneuver]]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> ManeuverCarrier:
        return cast(ManeuverCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[ManeuverBlueprint]:
        return cast(ManeuverBlueprint, super().blueprint)