# src/assurance/toolkit/model/toolkit.py

"""
Module: assurance.toolkit.model.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import TeamHelperTable, ModelValidationToolkit
from domain import Team, TeamManifest



class TeamValidationToolkit(ModelValidationToolkit[Team]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Team attribute validators and type metadata.

    Attributes:
        helper: Optional[TeamManifest]
        metadata: Optional[TeamHelperTable]

    Provides:

    Super Class:
    """
    _metadata: TeamManifest
    _helper: TeamHelperTable
    
    def __init__(
            self,
            metadata: Optional[TeamManifest] | None = None,
            helper: Optional[TeamHelperTable] | None = None,
    ):
        """
        Args:
            helper: Optional[TeamManifest]
            metadata: Optional[TeamHelperTable]
        """
        super().__init__(
            helper=helper or TeamHelperTable(),
            metadata=metadata or TeamManifest(),
        )
    
    @property
    def helper(self) -> TeamHelperTable:
        return cast(TeamHelperTable, super().helper)
    
    @property
    def metadata(self) -> TeamManifest:
        return cast(TeamManifest, super().metadata)
