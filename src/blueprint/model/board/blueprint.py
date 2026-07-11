# src/blueprint/model/board/blueprint.py

"""
Module: blueprint.model.board.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Type

from blueprint import ModelBlueprint
from err import BoardNullException
from model import Arena, Board


@dataclass
class BoardBlueprint(ModelBlueprint[Board]):
    """
    Role:
        -   Container
        -   DTO
        
    Responsibilities:
        1.  Provides values for instantiating a Board object.
    
    Attributes:
        id: Optional[int]
        arena: Arena
        
    Provides:
    
    Super Class:
        Blueprint
    """
    arena: Arena
    id: Optional[int] = None
    null_exception: BoardNullException = BoardNullException()
    model_class: Board = Type[Board]
    owner_name: str = type(owner).__name__
    

