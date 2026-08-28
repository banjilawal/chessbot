# src/domain/metadata/blueprint/model/searchable/state/board/blueprint.py

"""
Module: domain.metadata.blueprint.model.searchable.state.board.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Type

from domain.metadata.blueprint import StateModelBlueprint
from err import BoardNullException
from domain.model import Arena, Board


@dataclass
class BoardBlueprint(StateModelBlueprint[Board]):
    """
     Role:
        1.  Metadata
        
    Responsibilities:
        1.  Provides values for hydrating a Board object.
    
    Attributes:
        id: Optional[int]
        arena: Arena
        
    Provides:
    
    Super Class:
        Blueprint
    """
    arena: Arena
    id: Optional[int] = None
    domain_null_exception: BoardNullException = BoardNullException()
    domain_class: Board = Type[Board]
    owner_name: str = type(owner).__name__
    

