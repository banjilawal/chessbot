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

from blueprint import Blueprint
from engine import Engine
from model import Player


@dataclass
class PlayerBlueprint(Blueprint[Player]):
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
        Blueprint
     """
    name: Optional[str] = None
    engine: Optional[Engine] = None
    id: Optional[int] = None