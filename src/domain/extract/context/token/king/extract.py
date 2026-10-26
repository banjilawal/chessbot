# src/domain/extract/context/token/king.extract.py

"""
Module: domain.extract.context.token.king.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import KingToken, KingTokenContextBlueprint, TokenContextPrimeExtract
from transit import KingTokenContextCarrier


class KingTokenContextPrimeExtract(TokenContextPrimeExtract[KingTokenContext]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist ContextBlueprint and ContextCarrier data for KingTokenValidator.

    Attributes:
        contextCarrier: KingTokenContextCarrier
        blueprint: Optional[KingTokenContextBlueprint]

    Provides:

    Super Class:
        TokenContextPrimeExtract
    """

    def __init__(
            self,
            reference: KingTokenContextCarrier,
            blueprint: Optional[KingTokenContextBlueprint] | None = None,
    ):
        """
        Args:
            reference: KingTokenContextCarrier
            blueprint: Optional[KingTokenContextBlueprint]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> KingTokenContextCarrier:
        return cast(KingTokenContextCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[KingTokenContextBlueprint]:
        return cast(KingTokenContextBlueprint, super().blueprint)