# src/domain/metadata/nulls/model/token/roster.py

"""
Module: domain.metadata.nulls.model.token.roster
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass

from domain import ModelNullExceptionRoster, Token
from err import (
    TokenBlueprintNullException, TokenCarrierNullException, TokenSearchContextNullException, TokenNullException
)


@dataclass
class TokenNullExceptionRoster(ModelNullExceptionRoster[Token]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a Token.

    Attributes:
        model: TokenNullException
        carrier: TokenCarrierNullException
        blueprint: TokenBlueprintNullException
        search_context: TokenContextNullException

    Provides:

    Super Class:
        ModelNullExceptionRoster
    """
    model: TokenNullException = TokenNullException()
    carrier: TokenCarrierNullException = TokenCarrierNullException()
    blueprint: TokenBlueprintNullException = TokenBlueprintNullException()
    search_context: TokenSearchContextNullException = TokenSearchContextNullException()