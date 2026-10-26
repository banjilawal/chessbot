# src/domain/metadata/manifest/struct/binder/team/manifest.py

"""
Module: domain.metadata.manifest.struct.binder.team.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import BinderManifest, TeamBinder, TeamBinderNullGroup, TeamBinderLayer


class TeamBinderManifest(BinderManifest[TeamBinder]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for the TeamBinder
            security lifecycle.

     Attributes:
        types: TeamBinderTypeUnion
        nulls: TeamBinderNullGroup

     Provides:

     Super Class:
        ObjectManifest
     """
    
    def __init__(
            self,
            types: Optional[TeamBinderLayer] | None = None,
            nulls: Optional[TeamBinderNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[TeamBinderTypeUnion]
            nulls: Optional[TeamBinderNullGroup]
        """
        super().__init__(
            types=types or TeamBinderLayer(),
            nulls=nulls or TeamBinderNullGroup(),
        )
        
    @property
    def types(self) -> TeamBinderLayer:
        return cast(TeamBinderLayer, super().types)
    
    @property
    def nulls(self) -> TeamBinderNullGroup:
        return cast(TeamBinderNullGroup, super().nulls)