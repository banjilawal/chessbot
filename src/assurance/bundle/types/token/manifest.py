# src/assurance/manifest/types/token/manifest.py

"""
Module: assurance.manifest.types.token.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 1.0.1
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from assurance import TypesManifest
from fabrication import TokenBlueprint
from model import Token
from transit import TokenCarrier


@dataclass(frozen=True)
class TokenTypes(TypesManifest[Token]):
    model: Type[Token] = Token
    carrier: Type[TokenCarrier] = TokenCarrier
    blueprint: Type[TokenBlueprint] = TokenBlueprint