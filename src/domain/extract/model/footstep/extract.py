# src/domain/extract/model/footstep.extract.py

"""
Module: domain.extract.model.footstep.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Footstep, FootstepBlueprint, ModelPrimeExtract
from transit import FootstepCarrier


class FootstepPrimeExtract(ModelPrimeExtract[Footstep]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for FootstepValidator.

    Attributes:
        carrier: FootstepCarrier
        blueprint: Optional[FootstepBlueprint]

    Provides:

    Super Class:
        ModelPrimeExtract
    """

    def __init__(
            self,
            reference: FootstepCarrier,
            blueprint: Optional[FootstepBlueprint] | None = None,
    ):
        """
        Args:
            reference: FootstepCarrier
            blueprint: Optional[FootstepBlueprint]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> FootstepCarrier:
        return cast(FootstepCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[FootstepBlueprint]:
        return cast(FootstepBlueprint, super().blueprint)