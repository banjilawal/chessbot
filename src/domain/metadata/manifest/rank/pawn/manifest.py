# src/domain/metadata/manifest/rank/pawn/manifest.py

"""
Module: domain.metadata.manifest.rank.pawn.manifest
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
         1.  Aggregates NullExceptions and TypeUnions for an Pawn's security lifecycle.

     Attributes:
        type_union: PawnTypeUnion
        null_group: PawnNullGroup

     Provides:

     Super Class:
        RankManifest
     """
    
    def __init__(
            self,
            type_union: Optional[PawnTypeUnion] | None = None,
            null_group: Optional[PawnNullGroup] | None = None,
    ):
        """
        Args:
            type_union: Optional[PawnTypeUnion]
            null_group: Optional[PawnNullGroup]
        """
        super().__init__(
            type_union=type_union or PawnTypeUnion(),
            null_group=null_group or PawnNullGroup(),
        )
        
    @property
    def types(self) -> PawnTypeUnion:
        return cast(PawnTypeUnion, super().types)
    
    @property
    def nulls(self) -> PawnNullGroup:
        return cast(PawnNullGroup, super().nulls)