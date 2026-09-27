# src/domain/extract/model/token/pawn.extract.py

"""
Module: domain.extract.model.token.pawn.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import pawnToken, pawnTokenBlueprint, TokenPrimeExtract
from transit import pawnTokenCarrier


class pawnTokenPrimeExtract(TokenPrimeExtract[pawnToken]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for pawnTokenValidator.

    Attributes:
        carrier: pawnTokenCarrier
        blueprint: Optional[pawnTokenBlueprint]

    Provides:
        blueprint_exists: bool
        no_blueprint_exists: bool

    Super Class:
        TokenPrimeExtract
    """

    def __init__(
            self,
            carrier: pawnTokenCarrier,
            blueprint: Optional[pawnTokenBlueprint] | None = None,
    ):
        """
        Args:
            carrier: pawnTokenCarrier
            blueprint: Optional[pawnTokenBlueprint]
        """
        super().__init__(carrier=carrier, blueprint=blueprint,)
        
    @property
    def carrier(self) -> pawnTokenCarrier:
        return cast(pawnTokenCarrier, super().carrier)
    
    @property
    def blueprint(self) -> Optional[pawnTokenBlueprint]:
        return cast(pawnTokenBlueprint,super().blueprint)