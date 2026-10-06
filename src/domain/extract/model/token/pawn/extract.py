# src/domain/extract/model/token/pawn.extract.py

"""
Module: domain.extract.model.token.pawn.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import PawnToken, PawnTokenBlueprint, TokenPrimeExtract
from transit import PawnTokenCarrier


class PawnTokenPrimeExtract(TokenPrimeExtract[PawnToken]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for PawnTokenValidator.

    Attributes:
        carrier: PawnTokenCarrier
        blueprint: Optional[PawnTokenBlueprint]

    Provides:

    Super Class:
        TokenPrimeExtract
    """

    def __init__(
            self,
            reference: PawnTokenCarrier,
            blueprint: Optional[PawnTokenBlueprint] | None = None,
    ):
        """
        Args:
            reference: PawnTokenCarrier
            blueprint: Optional[PawnTokenBlueprint]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> PawnTokenCarrier:
        return cast(PawnTokenCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[PawnTokenBlueprint]:
        return cast(PawnTokenBlueprint, super().blueprint)