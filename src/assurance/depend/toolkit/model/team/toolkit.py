# src/assurance/depend/toolkit/model/team/toolkit.py

"""
Module: assurance.depend.toolkit.model.team.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelLayerToolkit, TeamServiceDependency
from domain import Team, TeamManifest, TeamNullWarningSet, TeamLayer


class TeamLayerToolkit(ModelLayerToolkit[Team]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Team attribute validators and type manifest.

    Attributes:
        helper: TeamManifest
        manifest: TeamServiceDependency

    Provides:

    Super Class:
        ModelLayerToolkit
    """
    
    def __init__(
            self,
            manifest: Optional[TeamManifest] | None = None,
            dependency: Optional[TeamServiceDependency] | None = None,
    ):
        """
        Args:
            dependency: Optional[TeamManifest]
            manifest: Optional[TeamServiceDependency]
        """
        super().__init__(
            dependency=dependency or TeamServiceDependency(),
            manifest=manifest or TeamManifest(),
        )
    
    @property
    def dependency(self) -> TeamServiceDependency:
        return cast(TeamServiceDependency, super().dependency)
    
    @property
    def manifest(self) -> TeamManifest:
        return cast(TeamManifest, super().manifest)
    
    @property
    def nulls(self) -> TeamNullWarningSet:
        return self.manifest.nulls
    
    @property
    def types(self) -> TeamLayer:
        return self.manifest.types
