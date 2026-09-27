# src/domain/extract/model/token/combatant.extract.py

"""
Module: domain.extract.model.token.combatant.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import combatantToken, combatantTokenBlueprint, TokenPrimeExtract
from transit import combatantTokenCarrier


class combatantTokenPrimeExtract(TokenPrimeExtract[combatantToken]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for combatantTokenValidator.

    Attributes:
        carrier: combatantTokenCarrier
        blueprint: Optional[combatantTokenBlueprint]

    Provides:
        blueprint_exists: bool
        no_blueprint_exists: bool

    Super Class:
        TokenPrimeExtract
    """

    def __init__(
            self,
            carrier: combatantTokenCarrier,
            blueprint: Optional[combatantTokenBlueprint] | None = None,
    ):
        """
        Args:
            carrier: combatantTokenCarrier
            blueprint: Optional[combatantTokenBlueprint]
        """
        super().__init__(carrier=carrier, blueprint=blueprint,)
        
    @property
    def carrier(self) -> combatantTokenCarrier:
        return cast(combatantTokenCarrier, super().carrier)
    
    @property
    def blueprint(self) -> Optional[combatantTokenBlueprint]:
        return cast(combatantTokenBlueprint,super().blueprint)