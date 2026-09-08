# src/domain/metadata/nulls/model/team/group.py

"""
Module: domain.metadata.nulls.model.team.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import NullExceptionGroup
from err import (
    TeamBlueprintNullException, TeamCarrierNullException, TeamNullException
)


class TeamNullGroup(NullExceptionGroup):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with an Team's integrity cycle.

    Attributes:
        model: TeamNullException
        carrier: TeamCarrierNullException
        blueprint: TeamBlueprintNullException

    Provides:

    Super Class:
        NullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[TeamNullException] | None = None,
            carrier: Optional[TeamCarrierNullException] | None = None,
            blueprint: Optional[TeamBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[TeamNullException]
            carrier: Optional[TeamCarrierNullException]
            blueprint: Optional[TeamBlueprintNullException]
        """
        super().__init__(
            model = model or TeamNullException(),
            carrier = carrier or TeamCarrierNullException(),
            blueprint = blueprint or TeamBlueprintNullException(),
        )
        
    @property
    def model(self) -> TeamNullException:
        return cast(TeamNullException, super().model)
    
    @property
    def carrier(self) -> TeamCarrierNullException:
        return cast(TeamCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> TeamBlueprintNullException:
        return cast(TeamBlueprintNullException, super().blueprint)