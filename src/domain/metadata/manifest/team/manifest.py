# src/domain/metadata/manifest/team/manifest.py

"""
Module: domain.metadata.manifest.team.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Team, TeamNullGroup, TeamTypeUnion, ObjectManifest


class TeamManifest(ObjectManifest[Team]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for an Team's security lifecycle.

     Attributes:
        type_union: TeamTypeUnion
        null_group: TeamNullGroup

     Provides:

     Super Class:
        ObjectManifest
     """
    
    def __init__(
            self,
            type_union: Optional[TeamTypeUnion] | None = None,
            null_group: Optional[TeamNullGroup] | None = None,
    ):
        """
        Args:
            type_union: Optional[TeamTypeUnion]
            null_group: Optional[TeamNullGroup]
        """
        super().__init__(
            type_union=type_union or TeamTypeUnion(),
            null_group=null_group or TeamNullGroup(),
        )
        
    @property
    def types(self) -> TeamTypeUnion:
        return cast(TeamTypeUnion, super().types)
    
    @property
    def nulls(self) -> TeamNullGroup:
        return cast(TeamNullGroup, super().nulls)