# src/domain/extract/model/token/extract.py

"""
Module: domain.extract.model.token.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelPrimeExtract
from domain import Token, TokenBlueprint
from transit import TokenCarrier


class TokenPrimeExtract(ModelPrimeExtract[Token]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for TokenValidator.

    Attributes:
        carrier: TokenCarrier
        blueprint: Optional[TokenBlueprint]

    Provides:
        blueprint_exists: bool
        no_blueprint_exists: bool

    Super Class:
        ModelPrimeExtract
    """

    def __init__(
            self,
            carrier: TokenCarrier,
            blueprint: Optional[TokenBlueprint] | None = None,
    ):
        """
        Args:
            carrier: EntityCarrier[Token]
            blueprint: Optional[Blueprint[Token]]
        """
        super().__init__(carrier=carrier, blueprint=blueprint,)
        
    @property
    def carrier(self) -> TokenCarrier:
        return cast(TokenCarrier, super().carrier)
    
    @property
    def blueprint(self) -> Optional[TokenBlueprint]:
        return cast(TokenBlueprint,super().blueprint)