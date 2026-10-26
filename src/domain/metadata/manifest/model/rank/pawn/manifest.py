# src/domain/metadata/manifest/model/rank/pawn/manifest.py

"""
Module: domain.metadata.manifest.model.rank.pawn.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Pawn, PawnNullWarningSet, PawnLayer, RankManifest


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
            types: Optional[PawnLayer] | None = None,
            nulls: Optional[PawnNullWarningSet] | None = None,
    ):
        """
        Args:
            types: Optional[PawnTypeUnion]
            nulls: Optional[PawnNullGroup]
        """
        super().__init__(
            types=types or PawnLayer(),
            nulls=nulls or PawnNullWarningSet(),
        )
        
    @property
    def types(self) -> PawnLayer:
        return cast(PawnLayer, super().types)
    
    @property
    def nulls(self) -> PawnNullWarningSet:
        return cast(PawnNullWarningSet, super().nulls)