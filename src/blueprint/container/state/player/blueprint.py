# src/blueprint/container/state/player/blueprint.py

"""
Module: blueprint.container.state.player.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Type

from blueprint import StateContainerBlueprint
from engine import Engine
from err import PlayerNullException
from container import Player


@dataclass
class PlayerBlueprint(StateContainerBlueprint[Player]):
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
        StateContainerBlueprint
     """
    name: Optional[str] = None
    engine: Optional[Engine] = None
    id: Optional[int] = None
    null_exception: PlayerNullException = PlayerNullException()
    container_class: Player = Type[Player]
    owner_name: str = type(owner).__name__