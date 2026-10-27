# src/assurance/depend/toolkit/struct/binder/team/toolkit.py

"""
Module: assurance.depend.toolkit.struct.binder.team.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import BinderLayerToolkit, TeamBinderDependency
from domain import (
    TeamBinder, TeamBinderManifest, TeamBinderNullGroup,
    TeamBinderLayer
)


class TeamBinderLayerToolkit(BinderLayerToolkit[TeamBinder]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for attribute validators and type manifest.

    Attributes:
            wrapper: TeamBinderDependency
            manifest: TeamBinderManifest

    Provides:

    Super Class:
       BinderLayerToolkit
    """
    
    def __init__(
            self,
            dependency: Optional[TeamBinderDependency] | None = None,
            manifest: Optional[TeamBinderManifest] | None = None,
    ):
        """
            wrapper: Optional[TeamBinderDependency]
            manifest: Optional[TeamBinderManifest]
        """
        super().__init__(
            dependency=dependency or TeamBinderDependency(),
            manifest=manifest or TeamBinderManifest(),
        )
    
    @property
    def dependency(self) -> TeamBinderDependency:
        return cast(TeamBinderDependency, super().dependency)
    
    @property
    def manifest(self) -> TeamBinderManifest:
        return cast(TeamBinderManifest, super().manifest)
    
    @property
    def nulls(self) -> TeamBinderNullGroup:
        return self.manifest.nulls
    
    @property
    def types(self) -> TeamBinderLayer:
        return self.manifest.types