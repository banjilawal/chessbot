# src/domain/metadata/blueprint/model/state/player/blueprint.py

"""
Module: domain.metadata.blueprint.model.state.player.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Type

from domain.metadata.blueprint import StateModelBlueprint
from engine import Engine
from err import PlayerNullException
from domain.model import Player


@dataclass
class PlayerBlueprint(StateModelBlueprint[Player]):
    """
    Role:
        - Container
        -  DTO

    Responsibilities:
        1.  Provides values for hydrating a Player object.

    Attributes:
        id: Optional[int]
        name: str
        engine: Engine

    Provides:

     Super Class:
        StateModelBlueprint
     """
    name: Optional[str] = None
    engine: Optional[Engine] = None
    id: Optional[int] = None
    domain_null_exception: PlayerNullException = PlayerNullException()
    domain_class: Player = Type[Player]
    owner_name: str = type(owner).__name__