# src/blueprint/model/player/blueprint.py

"""
Module: blueprint.model.player.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Type

from blueprint import ModelBlueprint
from engine import Engine
from err import PlayerNullException
from model import Player


@dataclass
class PlayerBlueprint(ModelBlueprint[Player]):
    """
    Role:
        -   Container
        -   DTO

    Responsibilities:
        1.  Provides values for instantiating a Player object.

    Attributes:
        id: Optional[int]
        name: str
        engine: Engine

    Provides:

     Super Class:
        ModelBlueprint
     """
    name: Optional[str] = None
    engine: Optional[Engine] = None
    id: Optional[int] = None
    null_exception: PlayerNullException = PlayerNullException()
    model_class: Player = Type[Player]
    owner_name: str = type(owner).__name__