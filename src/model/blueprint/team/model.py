# src/model/blueprint/team/model.py

"""
Module: model.blueprint.team.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from err import TeamNullException
from model.catalog import Schema
from model import Blueprint, Board, Player, Team

@dataclass
class TeamBlueprint(Blueprint[Team]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides values for instantiating a Team object.

    Attributes:
        id: Optional[int]
        owner: Player
        board: Board
        schema: Schema
        model_type: Team
        null_exception: TeamNullException
        
    Provides:

     Super Class:
        Blueprint
     """
    owner: Player
    board: Board
    schema: Schema
    id: Optional[int] | None = None
    null_exception: TeamNullException = TeamNullException()
    model_type: Team = Team
    

