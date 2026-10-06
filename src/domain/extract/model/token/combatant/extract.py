# src/domain/extract/model/token/combatant.extract.py

"""
Module: domain.extract.model.token.combatant.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import CombatantToken, CombatantTokenBlueprint, TokenPrimeExtract
from transit import CombatantTokenCarrier


class CombatantTokenPrimeExtract(TokenPrimeExtract[CombatantToken]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for CombatantTokenValidator.

    Attributes:
        carrier: CombatantTokenCarrier
        blueprint: Optional[CombatantTokenBlueprint]

    Provides:

    Super Class:
        TokenPrimeExtract
    """

    def __init__(
            self,
            reference: CombatantTokenCarrier,
            blueprint: Optional[CombatantTokenBlueprint] | None = None,
    ):
        """
        Args:
            reference: CombatantTokenCarrier
            blueprint: Optional[CombatantTokenBlueprint]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> CombatantTokenCarrier:
        return cast(CombatantTokenCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[CombatantTokenBlueprint]:
        return cast(CombatantTokenBlueprint, super().blueprint)