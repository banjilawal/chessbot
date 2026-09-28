# src/domain/extract/model/attack/extract.py

"""
Module: domain.extract.model.attack.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelPrimeExtract
from domain import Encounter, AttackBlueprint
from transit import AttackCarrier


class AttackPrimeExtract(ModelPrimeExtract[Encounter]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for AttackValidator.

    Attributes:
        carrier: AttackCarrier
        blueprint: Optional[AttackBlueprint]

    Provides:
        blueprint_exists: bool
        no_blueprint_exists: bool

    Super Class:
        ModelPrimeExtract
    """

    def __init__(
            self,
            carrier: AttackCarrier,
            blueprint: Optional[AttackBlueprint] | None = None,
    ):
        """
        Args:
            carrier: EntityCarrier[Attack]
            blueprint: Optional[Blueprint[Attack]]
        """
        super().__init__(carrier=carrier, blueprint=blueprint,)
        
    @property
    def carrier(self) -> AttackCarrier:
        return cast(AttackCarrier, super().carrier)
    
    @property
    def blueprint(self) -> Optional[AttackBlueprint]:
        return cast(AttackBlueprint,super().blueprint)