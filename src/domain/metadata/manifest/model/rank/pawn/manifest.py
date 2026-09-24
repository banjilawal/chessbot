# src/domain/metadata/manifest/model/rank/pawn/manifest.py

"""
Module: domain.metadata.manifest.model.rank.pawn.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Pawn, PawnNullGroup, PawnTypeUnion, RankManifest


class PawnManifest(RankManifest[Pawn]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for the Pawn security lifecycle.

     Attributes:
        types: PawnTypeUnion
        nulls: PawnNullGroup

     Provides:

     Super Class:
        RankManifest
     """
    
    def __init__(
            self,
            types: Optional[PawnTypeUnion] | None = None,
            nulls: Optional[PawnNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[PawnTypeUnion]
            nulls: Optional[PawnNullGroup]
        """
        super().__init__(
            types=types or PawnTypeUnion(),
            nulls=nulls or PawnNullGroup(),
        )
        
    @property
    def types(self) -> PawnTypeUnion:
        return cast(PawnTypeUnion, super().types)
    
    @property
    def nulls(self) -> PawnNullGroup:
        return cast(PawnNullGroup, super().nulls)