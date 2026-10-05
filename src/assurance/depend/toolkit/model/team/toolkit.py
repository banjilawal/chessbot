# src/assurance/depend/toolkit/model/team/toolkit.py

"""
Module: assurance.depend.toolkit.model.team.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelValidatorToolkit, TeamWrapperDependency
from domain import Team, TeamManifest, TeamNullGroup, TeamTypeUnion


class TeamValidatorToolkit(ModelValidatorToolkit[Team]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Team attribute validators and type metadata.

    Attributes:
        helper: TeamManifest
        metadata: TeamWrapperDependency

    Provides:

    Super Class:
        ModelValidatorToolkit
    """
    
    def __init__(
            self,
            metadata: Optional[TeamManifest] | None = None,
            wrapper: Optional[TeamWrapperDependency] | None = None,
    ):
        """
        Args:
            wrapper: Optional[TeamManifest]
            metadata: Optional[TeamWrapperDependency]
        """
        super().__init__(
            wrapper=wrapper or TeamWrapperDependency(),
            metadata=metadata or TeamManifest(),
        )
    
    @property
    def wrapper(self) -> TeamWrapperDependency:
        return cast(TeamWrapperDependency, super().wrapper)
    
    @property
    def metadata(self) -> TeamManifest:
        return cast(TeamManifest, super().metadata)
    
    @property
    def nulls(self) -> TeamNullGroup:
        return self.metadata.nulls
    
    @property
    def types(self) -> TeamTypeUnion:
        return self.metadata.types
