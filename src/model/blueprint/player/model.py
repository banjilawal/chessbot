# src/model/blueprint/player/model.py

"""
Module: model.blueprint.player.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from err import PlayerNullException
from logic.engine import Engine
from model import Blueprint, Player

@dataclass
class PlayerBlueprint(Blueprint[Player]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides values for instantiating a Player object.

    Attributes:
        id: Optional[int]
        name: str
        engine: Engine
        model_type: Player
        null_exception: PlayerNullException
        
    Provides:

     Super Class:
        Blueprint
     """
    name: Optional[str]
    engine: Optional[Engine]
    id: Optional[int] | None = None
    null_exception: PlayerNullException = PlayerNullException()
    model_type: Player = Player