# src/domain/extract/struct/token/extract.py

"""
Module: domain.extract.struct.token.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar, cast

from domain import StructPrimeExtract, Token, TokenBlueprint
from transit import TokenCarrier

T = TypeVar("T", bound="Token")

class TokenPrimeExtract(StructPrimeExtract[T], ABC, Generic[T]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for TokenValidator.

    Attributes:
        carrier: TokenCarrier
        blueprint: Optional[TokenBlueprint]

    Provides:

    Super Class:
        StructPrimeExtract
    """

    def __init__(
            self,
            carrier: TokenCarrier[T],
            blueprint: Optional[TokenBlueprint[T]] | None = None,
    ):
        """
        Args:
            carrier: TokenCarrier[T]
            blueprint: Optional[TokenBlueprint[T]]
        """
        super().__init__(carrier=carrier, blueprint=blueprint)
        
    @property
    def carrier(self) -> TokenCarrier[T]:
        return cast(TokenCarrier, super().carrier)
    
    @property
    def blueprint(self) -> Optional[TokenBlueprint[T]]:
        return cast(TokenBlueprint, super().blueprint)