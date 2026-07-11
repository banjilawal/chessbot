# src/blueprint/model/team/blueprint.py

"""
Module: blueprint.model.team.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, Type

from blueprint import ModelBlueprint
from model import Board, Player, Team
from schema import Archetype



class TeamBlueprint(ModelBlueprint[Team]):
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
        archetype: Archetype
        
    Provides:

     Super Class:
        ModelBlueprint
     """
    """
    Args:
        owner: Player
        board: Board
        archetype: Archetype
        id: Optional[int]
        owner: Team
        owner_name: str
    """
    ownerr: Player
    board: Board
    archetype: Archetype
    id: Optional[int] | None = None
    model_class: Type[Team] = Team
    owner_name: str = type(owner).__name__
    

