# src/domain/metadata/nulls/context/team/group.py

"""
Module: domain.metadata.nulls.context.team.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import ContextNullGroup, Team
from err import (
    TeamContextBlueprintNullException, TeamContextCarrierNullException, TeamContextNullException
)


class TeamContextNullGroup(ContextNullGroup[TeamContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with an Team's integrity cycle.

    Attributes:
        context: TeamContextNullException
        carrier: TeamContextCarrierNullException
        blueprint: TeamContextBlueprintNullException

    Provides:

    Super Class:
        ContextNullExceptionGroup
    """
    
    def __init__(
            self,
            context: Optional[TeamContextNullException] | None = None,
            carrier: Optional[TeamContextCarrierNullException] | None = None,
            blueprint: Optional[TeamContextBlueprintNullException] | None = None,
    ):
        """
        Args:
            context: Optional[TeamContextNullException]
            carrier: Optional[TeamContextCarrierNullException]
            blueprint: Optional[TeamContextBlueprintNullException]
        """
        super().__init__(
            context = context or TeamContextNullException(),
            carrier = carrier or TeamContextCarrierNullException(),
            blueprint = blueprint or TeamContextBlueprintNullException(),
        )
        
    @property
    def context(self) -> TeamContextNullException:
        return cast(TeamContextNullException, super().context)
    
    @property
    def carrier(self) -> TeamContextCarrierNullException:
        return cast(TeamContextCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> TeamContextBlueprintNullException:
        return cast(TeamContextBlueprintNullException, super().blueprint)