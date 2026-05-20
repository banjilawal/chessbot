# src/blueprint/validation/team/blueprint.py

"""
Module: blueprint.validation.query.team.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from blueprint import QueryValidationBlueprint
from err import TeamNullException
from model import Board, Blueprint, Player, Schema, Team, TeamValidation, TeamState


@dataclass
class TeamQueryValidationBlueprint(QueryValidationBlueprint[Team]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides values for instantiating a TeamValidation instance.

    Attributes:
        id: Optional[int]
        board: Optional[Board]
        player: Optional[Player]
        state: Optional[TeamState]
        schema: Optional[Schema]
        null_exception: TamNullException
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
    null_exception = TeamNullException()
    validation_model_type = TeamValidation
