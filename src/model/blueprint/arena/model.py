# src/model/blueprint/arena/model.py

"""
Module: model.blueprint.arena.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from err import ArenaNullException
from model import Game, Blueprint, Arena

@dataclass
class ArenaBlueprint(Blueprint[Arena]):
    """
    Role:
        -   Container
    
    Responsibilities:
        1.  Provides values for instantiating a Arena object.
    
    Attributes:
        id: Optional[int]
        game: Game
        model_type: Arena
        null_exception: ArenaNullException
        
    Provides:
    
    Super Class:
        Blueprint
    """
    game: Game
    id: Optional[int] | None = None
    null_exception: ArenaNullException = ArenaNullException()
    model_type: Arena = Arena

