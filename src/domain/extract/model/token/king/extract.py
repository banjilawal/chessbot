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
        blueprint_exists: bool
        no_blueprint_exists: bool

    Super Class:
        TokenPrimeExtract
    """

    def __init__(
            self,
            carrier: KingTokenCarrier,
            blueprint: Optional[KingTokenBlueprint] | None = None,
    ):
        """
        Args:
            carrier: KingTokenCarrier
            blueprint: Optional[KingTokenBlueprint]
        """
        super().__init__(carrier=carrier, blueprint=blueprint,)
        
    @property
    def carrier(self) -> KingTokenCarrier:
        return cast(KingTokenCarrier, super().carrier)
    
    @property
    def blueprint(self) -> Optional[KingTokenBlueprint]:
        return cast(KingTokenBlueprint,super().blueprint)