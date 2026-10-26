# src/domain/extract/context/token/combatant.extract.py

"""
Module: domain.extract.context.token.combatant.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import CombatantToken, CombatantTokenContextBlueprint, TokenContextPrimeExtract
from transit import CombatantTokenContextCarrier


class CombatantTokenContextPrimeExtract(TokenContextPrimeExtract[CombatantTokenContext]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist ContextBlueprint and ContextCarrier data for CombatantTokenValidator.

    Attributes:
        contextCarrier: CombatantTokenContextCarrier
        blueprint: Optional[CombatantTokenContextBlueprint]

    Provides:

    Super Class:
        TokenContextPrimeExtract
    """

    def __init__(
            self,
            reference: CombatantTokenContextCarrier,
            blueprint: Optional[CombatantTokenContextBlueprint] | None = None,
    ):
        """
        Args:
            reference: CombatantTokenContextCarrier
            blueprint: Optional[CombatantTokenContextBlueprint]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> CombatantTokenContextCarrier:
        return cast(CombatantTokenContextCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[CombatantTokenContextBlueprint]:
        return cast(CombatantTokenContextBlueprint, super().blueprint)