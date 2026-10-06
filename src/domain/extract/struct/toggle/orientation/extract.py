# src/domain/extract/struct/toggle/orientation/extract.py

"""
Module: domain.extract.struct.toggle.orientation.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Orientation, OrientationBlueprint, TogglePrimeExtract
from transit import OrientationCarrier


class OrientationTogglePrimeExtract(TogglePrimeExtract[Orientation]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for OrientationValidator.

    Attributes:
        carrier: OrientationCarrier
        blueprint: Optional[OrientationBlueprint]

    Provides:

    Super Class:
        TogglePrimeExtract
    """

    def __init__(
            self,
            carrier: OrientationCarrier,
            blueprint: Optional[OrientationBlueprint] | None = None,
    ):
        """
        Args:
            carrier: OrientationCarrier
            blueprint: Optional[OrientationBlueprint]
        """
        super().__init__(carrier=carrier, blueprint=blueprint)
        
    @property
    def carrier(self) -> OrientationCarrier:
        return cast(OrientationCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[OrientationBlueprint]:
        return cast(OrientationBlueprint, super().blueprint)