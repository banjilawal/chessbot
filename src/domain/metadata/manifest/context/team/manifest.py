# src/domain/metadata/context/manifest/context/team/manifest.py

"""
Module: domain.metadata.manifest.context.team.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Team, TeamContextNullGroup, TeamContextLayer, ContextManifest


class TeamContextManifest(ContextManifest[Team]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and ContextTypeUnions for the Team security lifecycle.

     Attributes:
        types: TeamContextTypeUnion
        nulls: TeamContextNullGroup

     Provides:

     Super Class:
        ContextManifest
     """
    
    def __init__(
            self,
            types: Optional[TeamContextLayer] | None = None,
            nulls: Optional[TeamContextNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[TeamContextTypeUnion]
            nulls: Optional[TeamContextNullGroup]
        """
        super().__init__(
            types=types or TeamContextLayer(),
            nulls=nulls or TeamContextNullGroup(),
        )
        
    @property
    def types(self) -> TeamContextLayer:
        return cast(TeamContextLayer, super().types)
    
    @property
    def nulls(self) -> TeamContextNullGroup:
        return cast(TeamContextNullGroup, super().nulls)