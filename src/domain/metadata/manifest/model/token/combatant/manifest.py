# src/domain/metadata/manifest/model/token/combatant/manifest.py

"""
Module: domain.metadata.manifest.model.token.combatant.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import (
    CombatantTokenNullWarningSet, CombatantToken, TokenManifest, CombatantTokenLayer
)


class CombatantTokenManifest(TokenManifest[CombatantToken]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1. Aggregates NullExceptions and TypeUnions for the CombatantToken
            security lifecycle.

     Attributes:
        types: CombatantTokenTypeUnion
        nulls: CombatantTokenNullGroup

     Provides:

     Super Class:
        TokenManifest
     """
    
    def __init__(
            self,
            types: Optional[CombatantTokenLayer] | None = None,
            nulls: Optional[CombatantTokenNullWarningSet] | None = None,
    ):
        """
        Args:
            types: Optional[CombatantTokenTypeUnion]
            nulls: Optional[CombatantTokenNullGroup]
        """
        super().__init__(
            types=types or CombatantTokenLayer(),
            nulls=nulls or CombatantTokenNullWarningSet(),
        )
    
    @property
    def types(self) -> CombatantTokenLayer:
        return cast(CombatantTokenLayer, super().types)
    
    @property
    def nulls(self) -> CombatantTokenNullWarningSet:
        return cast(CombatantTokenNullWarningSet, super().nulls)