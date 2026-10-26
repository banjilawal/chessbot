# src/domain/extract/context/token/pawn.extract.py

"""
Module: domain.extract.context.token.pawn.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import PawnToken, PawnTokenContextBlueprint, TokenContextPrimeExtract
from transit import PawnTokenContextCarrier


class PawnTokenContextPrimeExtract(TokenContextPrimeExtract[PawnTokenContext]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist ContextBlueprint and ContextCarrier data for PawnTokenValidator.

    Attributes:
        contextCarrier: PawnTokenContextCarrier
        blueprint: Optional[PawnTokenContextBlueprint]

    Provides:

    Super Class:
        TokenContextPrimeExtract
    """

    def __init__(
            self,
            reference: PawnTokenContextCarrier,
            blueprint: Optional[PawnTokenContextBlueprint] | None = None,
    ):
        """
        Args:
            reference: PawnTokenContextCarrier
            blueprint: Optional[PawnTokenContextBlueprint]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> PawnTokenContextCarrier:
        return cast(PawnTokenContextCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[PawnTokenContextBlueprint]:
        return cast(PawnTokenContextBlueprint, super().blueprint)