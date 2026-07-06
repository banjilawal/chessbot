# src/blueprint/model/arena/blueprint.py

"""
Module: blueprint.model.arena.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from blueprint import Blueprint
from model import Arena, Game


@dataclass
class ArenaBlueprint(Blueprint[Arena]):
    """
    Role:
        -   Container
        -   DTO
    
    Responsibilities:
        1.  Provides values for instantiating a Arena object.
    
    Attributes:
        id: Optional[int]
        game: Game
        
    Provides:
    
    Super Class:
        Blueprint
    """
    game: Game
    id: Optional[int] | None = None

