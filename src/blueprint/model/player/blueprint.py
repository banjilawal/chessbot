# src/blueprint/model/player/blueprint.py

"""
Module: blueprint.model.player.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from engine import Engine
from err import PlayerNullException
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