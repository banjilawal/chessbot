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

from blueprint import Blueprint
from err import BoardNullException
from model import Arena, Board


@dataclass
class BoardBlueprint(Blueprint[Board]):
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

    

