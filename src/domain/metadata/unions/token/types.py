# src/domain/metadata/unions/token/manifest.py

"""
Module: domain.metadata.unions.token.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from domain import Token, TokenBlueprint, TypeUnion
from transit import TokenCarrier


@dataclass
class TokenTypeUnion(TypeUnion[Token]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of data unions an Token uses in the domain.

    Attributes:
        model: Type[Token] = Token
        carrier: Type[TokenCarrier] = TokenCarrier
        blueprint: Type[TokenBlueprint] = TokenBlueprint
    
    Provides:

    Super Class:
        TypeUnion
    """
    model: Type[Token] = Token
    carrier: Type[TokenCarrier] = TokenCarrier
    blueprint: Type[TokenBlueprint] = TokenBlueprint