# src/domain/metadata/types/model/token/manifest.py

"""
Module: domain.metadata.types.model.token.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from domain import ModelAssociationManifest, Token, TokenBlueprint, TokenCarrier, TokenSearchContext


@dataclass
class TokenAssociationManifest(ModelAssociationManifest[Token]):
    """
    Role:
        -   Metadata

    Responsibilities:
        1. Catalog of data types a Token uses in the domain.

    Attributes:
        model: Type[Token] = Token
        carrier: Type[TokenCarrier] = TokenCarrier
        blueprint: Type[TokenBlueprint] = TokenBlueprint
        search_context: Type[TokenSearchContext] = TokenSearchContext
    
    Provides:

    Super Class:
        ModelManifest
    """
    model: Type[Token] = Token
    carrier: Type[TokenCarrier] = TokenCarrier
    blueprint: Type[TokenBlueprint] = TokenBlueprint
    search_context: Type[TokenSearchContext] = TokenSearchContext