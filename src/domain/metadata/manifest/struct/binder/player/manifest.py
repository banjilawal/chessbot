# src/domain/metadata/manifest/struct/binder/player/manifest.py

"""
Module: domain.metadata.manifest.struct.binder.player.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import BinderManifest, PlayerBinder, PlayerBinderNullGroup, PlayerBinderTypeUnion


class PlayerBinderManifest(BinderManifest[PlayerBinder]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for the PlayerBinder
            security lifecycle.

     Attributes:
        types: PlayerBinderTypeUnion
        nulls: PlayerBinderNullGroup

     Provides:

     Super Class:
        ObjectManifest
     """
    
    def __init__(
            self,
            types: Optional[PlayerBinderTypeUnion] | None = None,
            nulls: Optional[PlayerBinderNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[PlayerBinderTypeUnion]
            nulls: Optional[PlayerBinderNullGroup]
        """
        super().__init__(
            types=types or PlayerBinderTypeUnion(),
            nulls=nulls or PlayerBinderNullGroup(),
        )
        
    @property
    def types(self) -> PlayerBinderTypeUnion:
        return cast(PlayerBinderTypeUnion, super().types)
    
    @property
    def nulls(self) -> PlayerBinderNullGroup:
        return cast(PlayerBinderNullGroup, super().nulls)