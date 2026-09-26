# src/assurance/toolkit/model/team/toolkit.py

"""
Module: assurance.toolkit.model.team.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelValidatorToolkit, TeamBlueprintLoader, TeamValidationWrapperDict
from domain import Team, TeamManifest, TeamNullGroup, TeamTypeUnion


class TeamValidatorToolkit(ModelValidatorToolkit[Team]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Team attribute validators and type metadata.

    Attributes:
        helper: TeamManifest
        metadata: TeamHelperTable
        blueprint_loader: TeamBlueprintLoader

    Provides:

    Super Class:
        ModelValidatorToolkit
    """
    
    def __init__(
            self,
            metadata: Optional[TeamManifest] | None = None,
            wrapper: Optional[TeamValidationWrapperDict] | None = None,
            blueprint_loader: Optional[TeamBlueprintLoader] | None = None,
    ):
        """
        Args:
            wrapper: Optional[TeamManifest]
            metadata: Optional[TeamHelperTable]
            blueprint_loader: Optional[TeamBlueprintLoader]
        """
        super().__init__(
            wrapper=wrapper or TeamValidationWrapperDict(),
            metadata=metadata or TeamManifest(),
            blueprint_loader=blueprint_loader or TeamBlueprintLoader(),
        )
    
    @property
    def wrapper(self) -> TeamValidationWrapperDict:
        return cast(TeamValidationWrapperDict, super().wrapper)
    
    @property
    def metadata(self) -> TeamManifest:
        return cast(TeamManifest, super().metadata)
    
    @property
    def blueprint_loader(self) -> TeamBlueprintLoader:
        return cast(TeamBlueprintLoader, super().blueprint_loader)
    
    @property
    def nulls(self) -> TeamNullGroup:
        return self.metadata.nulls
    
    @property
    def types(self) -> TeamTypeUnion:
        return self.metadata.types
