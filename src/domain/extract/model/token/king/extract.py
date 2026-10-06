# src/domain/extract/model/token/king.extract.py

"""
Module: domain.extract.model.token.king.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import KingToken, KingTokenBlueprint, TokenPrimeExtract
from transit import KingTokenCarrier


class KingTokenPrimeExtract(TokenPrimeExtract[KingToken]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for KingTokenValidator.

    Attributes:
        carrier: KingTokenCarrier
        blueprint: Optional[KingTokenBlueprint]

    Provides:

    Super Class:
        TokenPrimeExtract
    """

    def __init__(
            self,
            reference: KingTokenCarrier,
            blueprint: Optional[KingTokenBlueprint] | None = None,
    ):
        """
        Args:
            reference: KingTokenCarrier
            blueprint: Optional[KingTokenBlueprint]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> KingTokenCarrier:
        return cast(KingTokenCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[KingTokenBlueprint]:
        return cast(KingTokenBlueprint, super().blueprint)