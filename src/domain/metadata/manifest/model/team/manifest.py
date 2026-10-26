# src/domain/metadata/manifest/model/team/manifest.py

"""
Module: domain.metadata.manifest.model.team.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Team, TeamNullGroup, TeamLayer, ModelManifest


class TeamManifest(ModelManifest[Team]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for the Team security lifecycle.

     Attributes:
        types: TeamTypeUnion
        nulls: TeamNullGroup

     Provides:

     Super Class:
        ModelManifest
     """
    
    def __init__(
            self,
            types: Optional[TeamLayer] | None = None,
            nulls: Optional[TeamNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[TeamTypeUnion]
            nulls: Optional[TeamNullGroup]
        """
        super().__init__(
            types=types or TeamLayer(),
            nulls=nulls or TeamNullGroup(),
        )
        
    @property
    def types(self) -> TeamLayer:
        return cast(TeamLayer, super().types)
    
    @property
    def nulls(self) -> TeamNullGroup:
        return cast(TeamNullGroup, super().nulls)