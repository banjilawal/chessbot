# src/blueprint/model/arena/blueprint.py

"""
Module: blueprint.model.arena.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Type

from blueprint import Blueprint
from err import ArenaNullException
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
    null_exception: ArenaNullException = ArenaNullException()
    owner: Arena = Type[Arena]
    owner_name: str = type(owner).__name__

