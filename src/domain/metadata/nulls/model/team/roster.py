# src/domain/metadata/nulls/model/team/roster.py

"""
Module: domain.metadata.nulls.model.team.roster
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass

from domain import ModelNullExceptionRoster, Team
from err import (
    TeamBlueprintNullException, TeamCarrierNullException, TeamStackContextNullException, TeamNullException
)


@dataclass
class TeamNullExceptionRoster(ModelNullExceptionRoster[Team]):
    """
    Role:
        -   Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a Team.

    Attributes:
        model: TeamNullException
        carrier: TeamCarrierNullException
        blueprint: TeamBlueprintNullException
        search_context: TeamContextNullException

    Provides:

    Super Class:
        ModelNullExceptionRoster
    """
    model: TeamNullException = TeamNullException()
    carrier: TeamCarrierNullException = TeamCarrierNullException()
    blueprint: TeamBlueprintNullException = TeamBlueprintNullException()
    search_context: TeamStackContextNullException = TeamStackContextNullException()