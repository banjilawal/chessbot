# src/assurance/manifest/bundle/token/manifest.py

"""
Module: assurance.manifest.bundle.token.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass

from assurance import Manifest, TokenExceptionManifest, TokenTypes
from model import Token


@dataclass(frozen=True)
class TokenManifest(Manifest[Token]):
    types: TokenTypes = TokenTypes()
    null_exceptions: TokenExceptionManifest = TokenExceptionManifest()