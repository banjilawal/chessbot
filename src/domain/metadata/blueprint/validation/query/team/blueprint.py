# src/domain/metadata/blueprint/validation/team/blueprint.py

"""
Module: domain.metadata.blueprint.validation.query.team.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from domain.metadata.blueprint import QueryValidationBlueprint
from err import TeamNullException
from domain.model import Board, Player, Schema, Team, TeamValidation, TeamState


@dataclass
class TeamQueryValidationBlueprint(QueryValidationBlueprint[Team]):
    """
     Role:
        1.  Metadata

    Responsibilities:
        1.  Provides values for hydrating a TeamValidation instance.

    Attributes:
        id: Optional[int]
        board: Optional[Board]
        player: Optional[Player]
        state: Optional[TeamState]
        schema: Optional[Schema]
        domain_null_exception: TamNullException
        validation_model_type = TeamValidation

    Provides:

    Super Class:
        QueryValidationBlueprint
    """
    id: Optional[int] = None | None
    board: Optional[Board] = None | None
    player: Optional[Player] = None | None
    state: Optional[TeamState] = None | None
    schema: Optional[Schema] = None | None
    domain_null_exception = TeamNullException()
    validation_model_type = TeamValidation
