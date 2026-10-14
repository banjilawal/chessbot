# src/assurance/depend/toolkit/struct/binder/team/toolkit.py

"""
Module: assurance.depend.toolkit.struct.binder.team.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import BinderValidatorToolkit, TeamBinderDependency
from domain import (
    TeamBinder, TeamBinderManifest, TeamBinderNullGroup,
    TeamBinderTypeUnion
)


class TeamBinderValidatorToolkit(BinderValidatorToolkit[TeamBinder]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for attribute validators and type metadata.

    Attributes:
            wrapper: TeamBinderDependency
            metadata: TeamBinderManifest

    Provides:

    Super Class:
       BinderValidatorToolkit
    """
    
    def __init__(
            self,
            wrapper: Optional[TeamBinderDependency] | None = None,
            metadata: Optional[TeamBinderManifest] | None = None,
    ):
        """
            wrapper: Optional[TeamBinderDependency]
            metadata: Optional[TeamBinderManifest]
        """
        super().__init__(
            wrapper=wrapper or TeamBinderDependency(),
            metadata=metadata or TeamBinderManifest(),
        )
    
    @property
    def wrapper(self) -> TeamBinderDependency:
        return cast(TeamBinderDependency, super().wrapper)
    
    @property
    def metadata(self) -> TeamBinderManifest:
        return cast(TeamBinderManifest, super().metadata)
    
    @property
    def nulls(self) -> TeamBinderNullGroup:
        return self.metadata.nulls
    
    @property
    def types(self) -> TeamBinderTypeUnion:
        return self.metadata.types