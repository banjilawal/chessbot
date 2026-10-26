# src/domain/metadata/null/context/token/null.py

"""
Module: domain.metadata.null.context.token.null
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, Optional, TypeVar, cast

from domain import ContextNullWarningSet, Token, TokenContext
from err import (
    TokenContextBlueprintNullException, TokenContextCarrierNullException, TokenContextNullException
)


class TokenContextNullWarningSet(ContextNullWarningSet[TokenContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with an Token's integrity cycle.

    Attributes:
        model: TokenContextNullException
        carrier: TokenContextCarrierNullException
        blueprint: TokenContextBlueprintNullException

    Provides:

    Super Class:
        ContextNullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[TokenContextNullException] | None = None,
            carrier: Optional[TokenContextCarrierNullException] | None = None,
            blueprint: Optional[TokenContextBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[TokenContextNullException]
            carrier: Optional[TokenContextCarrierNullException]
            blueprint: Optional[TokenContextBlueprintNullException]
        """
        super().__init__(
            model=model or TokenContextNullException(),
            carrier=carrier or TokenContextCarrierNullException(),
            blueprint=blueprint or TokenContextBlueprintNullException(),
        )
        
    @property
    def model(self) -> TokenContextNullException:
        return cast(TokenContextNullException, super().model)
    
    @property
    def carrier(self) -> TokenContextCarrierNullException:
        return cast(TokenContextCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> TokenContextBlueprintNullException:
        return cast(TokenContextBlueprintNullException, super().blueprint)