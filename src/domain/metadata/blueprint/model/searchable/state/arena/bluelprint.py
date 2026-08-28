# src/domain/metadata/blueprint/model/searchable/state/arena/blueprint.py

"""
Module: domain.metadata.blueprint.model.searchable.state.arena.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Type

from domain.metadata.blueprint import StateModelBlueprint
from err import ArenaNullException
from domain.model import Arena, Game


@dataclass
class ArenaBlueprint(StateModelBlueprint[Arena]):
    """
     Role:
        1.  Metadata
        -  DTO
    
    Responsibilities:
        1.  Provides values for hydrating a Arena object.
    
    Attributes:
        id: Optional[int]
        game: Game
        
    Provides:
    
    Super Class:
        Blueprint
    """
    game: Game
    id: Optional[int] | None = None
    domain_null_exception: ArenaNullException = ArenaNullException()
    domain_class: Arena = Type[Arena]
    owner_name: str = type(owner).__name__

