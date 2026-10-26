# src/domain/metadata/manifest/model/arena/manifest.py

"""
Module: domain.metadata.manifest.model.arena.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Arena, ArenaNullWarningSet, ArenaLayer, ModelManifest


class ArenaManifest(ModelManifest[Arena]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for the Arena security lifecycle.

     Attributes:
        types: ArenaTypeUnion
        nulls: ArenaNullGroup

     Provides:

     Super Class:
        ModelManifest
     """
    
    def __init__(
            self,
            types: Optional[ArenaLayer] | None = None,
            nulls: Optional[ArenaNullWarningSet] | None = None,
    ):
        """
        Args:
            types: Optional[ArenaTypeUnion]
            nulls: Optional[ArenaNullGroup]
        """
        super().__init__(
            types=types or ArenaLayer(),
            nulls=nulls or ArenaNullWarningSet(),
        )
        
    @property
    def types(self) -> ArenaLayer:
        return cast(ArenaLayer, super().types)
    
    @property
    def nulls(self) -> ArenaNullWarningSet:
        return cast(ArenaNullWarningSet, super().nulls)