# src/assurance/manifest/nulls/token/roster.py

"""
Module: assurance.manifest.nulls.token.roster
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass

from assurance import NullRoster
from err import TokenBlueprintNullException, TokenCarrierNullException, TokenNullException
from model import Token


@dataclass
class TokenNullRoster(NullRoster[Token]):
    model: TokenNullException = TokenNullException()
    carrier: TokenCarrierNullException = TokenCarrierNullException()
    blueprint: TokenBlueprintNullException = TokenBlueprintNullException()