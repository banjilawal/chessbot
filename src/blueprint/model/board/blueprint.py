# src/blueprint/model/board/blueprint.py

"""
Module: blueprint.model.board.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from err import BoardNullException
from model import Arena, Blueprint, Board

@dataclass
class BoardBlueprint(Blueprint[Board]):
    """
    Role:
        -   Container
    
    Responsibilities:
        1.  Provides values for instantiating a Board object.
    
    Attributes:
        id: Optional[int]
        arena: Arena
        model_type: Board
        null_exception: BoardNullException
    Provides:
    
    Super Class:
        Blueprint
    """
    arena: Arena
    id: Optional[int] | None = None
    null_exception: BoardNullException = BoardNullException()
    model_type: Board = Board
    

