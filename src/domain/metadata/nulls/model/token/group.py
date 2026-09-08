# src/domain/metadata/nulls/model/token/group.py

"""
Module: domain.metadata.nulls.model.token.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar, cast

from domain import NullExceptionGroup, Token
from err import (
    TokenBlueprintNullException, TokenCarrierNullException, TokenNullException
)

T = TypeVar("T", bound="Token")

class TokenNullGroup(NullExceptionGroup[T], ABC, Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with an Token's integrity cycle.

    Attributes:
        model: TokenNullException
        carrier: TokenCarrierNullException
        blueprint: TokenBlueprintNullException

    Provides:

    Super Class:
        NullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[TokenNullException] | None = None,
            carrier: Optional[TokenCarrierNullException] | None = None,
            blueprint: Optional[TokenBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[TokenNullException]
            carrier: Optional[TokenCarrierNullException]
            blueprint: Optional[TokenBlueprintNullException]
        """
        super().__init__(
            model = model or TokenNullException(),
            carrier = carrier or TokenCarrierNullException(),
            blueprint = blueprint or TokenBlueprintNullException(),
        )
        
    @property
    def model(self) -> TokenNullException:
        return cast(TokenNullException, super().model)
    
    @property
    def carrier(self) -> TokenCarrierNullException:
        return cast(TokenCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> TokenBlueprintNullException:
        return cast(TokenBlueprintNullException, super().blueprint)