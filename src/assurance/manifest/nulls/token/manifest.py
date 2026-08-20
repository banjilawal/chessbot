# src/assurance/manifest/nulls/token/manifest.py

"""
Module: assurance.manifest.nulls.token.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 1.0.1
"""

from __future__ import annotations


from dataclasses import dataclass

from assurance import NullExceptionManifest
from err import TokenBlueprintNullException, TokenCarrierNullException, TokenNullException
from model import Token


@dataclass(frozen=True)
class TokenExceptionManifest(NullExceptionManifest[Token]):
    model: TokenNullException = TokenNullException()
    carrier: TokenCarrierNullException = TokenCarrierNullException()
    blueprint: TokenBlueprintNullException = TokenBlueprintNullException()