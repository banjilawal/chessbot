# src/domain/metadata/types/token/manifest.py

"""
Module: domain.metadata.types.token.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from assurance import TypesManifest
from fabrication import TokenBlueprint
from domain.model import Token
from domain.transit import TokenCarrier


@dataclass
class TokenTypes(TypesManifest[Token]):
    model: Type[Token] = Token
    carrier: Type[TokenCarrier] = TokenCarrier
    blueprint: Type[TokenBlueprint] = TokenBlueprint