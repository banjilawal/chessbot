# src/blueprint/model/team/blueprint.py

"""
Module: blueprint.model.team.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from blueprint import Blueprint
from model import Board, Player, Schema, Team


@dataclass
class TeamBlueprint(Blueprint[Team]):
    """
    Role:
        -   Container
        -   DTO

    Responsibilities:
        1.  Provides values for instantiating a Team object.
        2.  DTO

    Attributes:
        id: Optional[int]
        owner: Player
        board: Board
        schema: Schema
        
    Provides:

     Super Class:
        Blueprint
     """
    owner: Player
    board: Board
    schema: Schema
    id: Optional[int] | None = None
    

