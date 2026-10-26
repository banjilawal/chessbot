# src/domain/metadata/context/manifest/context/arena/manifest.py

"""
Module: domain.metadata.manifest.context.arena.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Arena, ArenaContextNullGroup, ArenaContextTypeUnion, ContextManifest


class ArenaContextManifest(ContextManifest[Arena]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and ContextTypeUnions for the Arena security lifecycle.

     Attributes:
        types: ArenaContextTypeUnion
        nulls: ArenaContextNullGroup

     Provides:

     Super Class:
        ContextManifest
     """
    
    def __init__(
            self,
            types: Optional[ArenaContextTypeUnion] | None = None,
            nulls: Optional[ArenaContextNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[ArenaContextTypeUnion]
            nulls: Optional[ArenaContextNullGroup]
        """
        super().__init__(
            types=types or ArenaContextTypeUnion(),
            nulls=nulls or ArenaContextNullGroup(),
        )
        
    @property
    def types(self) -> ArenaContextTypeUnion:
        return cast(ArenaContextTypeUnion, super().types)
    
    @property
    def nulls(self) -> ArenaContextNullGroup:
        return cast(ArenaContextNullGroup, super().nulls)