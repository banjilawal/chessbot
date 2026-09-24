# src/domain/metadata/manifest/model/token/combatant/pawn/manifest.py

"""
Module: domain.metadata.manifest.model.token.combatant.pawn.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import CombatantTokenManifest, PawnTokenTokenNullGroup


class PawnTokenManifest(CombatantTokenManifest):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1. Aggregates NullExceptions and TypeUnions for the PawnToken
            security lifecycle.

     Attributes:
        types: PawnTokenTypeUnion
        nulls: PawnTokenNullGroup

     Provides:

     Super Class:
        CombatantTokenManifest
     """
    
    def __init__(
            self,
            types: Optional[PawnTokenTypeUnion] | None = None,
            nulls: Optional[PawnTokenTokenNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[PawnTokenTypeUnion]
            nulls: Optional[PawnTokenNullGroup]
        """
        super().__init__(
            types=types or PawnTokenTypeUnion(),
            nulls=nulls or PawnTokenTokenNullGroup(),
        )
    
    @property
    def types(self) -> PawnTokenTypeUnion:
        return cast(PawnTokenTypeUnion, super().types)
    
    @property
    def nulls(self) -> PawnTokenTokenNullGroup:
        return cast(PawnTokenTokenNullGroup, super().nulls)