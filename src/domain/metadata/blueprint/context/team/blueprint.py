# src/domain/metadata/blueprint/context/team/blueprint.py

"""
Module: domain.metadata.blueprint.context.team.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from err import TeamSearchContextNullException
from domain.model import Board, Blueprint, Player, Schema, TeamContext, TeamState


@dataclass
class TeamContextBlueprint(Blueprint[TeamContext]):
    """
     Role:
        1.  Metadata

    Responsibilities:
        1.  Provides values for hydrating a TeamContext instance.

    Attributes:
        id: Optional[int]
        board: Optional[Board]
        player: Optional[Player]
        state: Optional[TeamState]
        schema: Optional[Schema]
        domain_null_exception: TamContextNullException
        context_model_type = TeamContext

    Provides:

    Super Class:
        ContextBlueprint
    """
    id: Optional[int] = None | None
    board: Optional[Board] = None | None
    player: Optional[Player] = None | None
    state: Optional[TeamState] = None | None
    schema: Optional[Schema] = None | None
    domain_null_exception = TeamSearchContextNullException()
    context_model_type = TeamContext
