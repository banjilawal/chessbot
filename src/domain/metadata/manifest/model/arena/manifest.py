# src/domain/metadata/manifest/model/arena/manifest.py

"""
Module: domain.metadata.manifest.model.arena.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Arena, ArenaNullGroup, ArenaTypeUnion, ModelManifest


class ArenaManifest(ModelManifest[Arena]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for an Arena's security lifecycle.

     Attributes:
        types: ArenaTypeUnion
        nulls: ArenaNullGroup

     Provides:

     Super Class:
        ModelManifest
     """
    
    def __init__(
            self,
            types: Optional[ArenaTypeUnion] | None = None,
            nulls: Optional[ArenaNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[ArenaTypeUnion]
            nulls: Optional[ArenaNullGroup]
        """
        super().__init__(
            types=types or ArenaTypeUnion(),
            nulls=nulls or ArenaNullGroup(),
        )
        
    @property
    def types(self) -> ArenaTypeUnion:
        return cast(ArenaTypeUnion, super().types)
    
    @property
    def nulls(self) -> ArenaNullGroup:
        return cast(ArenaNullGroup, super().nulls)