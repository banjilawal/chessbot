# src/domain/extract/context/token/extract.py

"""
Module: domain.extract.context.token.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, Optional, TypeVar, cast

from domain import ContextPrimeExtract, Token, TokenContextBlueprint
from transit import TokenContextCarrier

T = TypeVar("T", bound="Token")


class TokenContextPrimeExtract(ContextPrimeExtract[T], Generic[TContext]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist ContextBlueprint and ContextCarrier data for TokenValidator.

    Attributes:
        contextCarrier: TokenContextCarrier
        blueprint: Optional[TokenContextBlueprint]

    Provides:

    Super Class:
        ContextPrimeExtract
    """
    
    def __init__(
            self,
            reference: TokenContextCarrier[T],
            blueprint: Optional[TokenContextBlueprint[T]] | None = None,
    ):
        """
        Args:
            reference: TokenContextCarrier[T]
            blueprint: Optional[TokenContextBlueprint[T]]
        """
        super().__init__(reference=reference, blueprint=blueprint)
    
    @property
    def reference(self) -> TokenContextCarrier[T]:
        return cast(TokenContextCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[TokenContextBlueprint[T]]:
        return cast(TokenContextBlueprint[T], super().blueprint)