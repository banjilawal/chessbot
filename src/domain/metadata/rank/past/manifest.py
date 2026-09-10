# src/domain/metadata/manifest/arena/manifest.py

"""
Module: domain.metadata.manifest.arena.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Arena, ArenaNullGroup, ArenaTypeUnion, ObjectManifest


class ArenaManifest(ObjectManifest[Arena]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for an Arena's security lifecycle.

     Attributes:
        type_union: ArenaTypeUnion
        null_group: ArenaNullGroup

     Provides:

     Super Class:
        ObjectManifest
     """
    
    def __init__(
            self,
            type_union: Optional[ArenaTypeUnion] | None = None,
            null_group: Optional[ArenaNullGroup] | None = None,
    ):
        """
        Args:
            type_union: Optional[ArenaTypeUnion]
            null_group: Optional[ArenaNullGroup]
        """
        super().__init__(
            type_union=type_union or ArenaTypeUnion(),
            null_group=null_group or ArenaNullGroup(),
        )
        
    @property
    def types(self) -> ArenaTypeUnion:
        return cast(ArenaTypeUnion, super().types)
    
    @property
    def nulls(self) -> ArenaNullGroup:
        return cast(ArenaNullGroup, super().nulls)