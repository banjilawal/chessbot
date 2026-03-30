# src/logic/zone/mode/model.py

"""
Module: logic.zone.model.model
Author: Banji Lawal
Created: 2026-03-29
version: 1.0.0
"""

from __future__ import annotations

from enum import Enum

from logic.schema import Schema
from logic.system import GameColor


class Zone(Enum):
    """
    Role:
        -   Addressing
        -   Data-Holder
  
    Responsibilities:
        1.  Provide global, low-level addressing squares and tokens on the board.
        
    Attributes:
        color: GameColor
        schema: Schema
        
    Provides:
        -   def opposite(zone: Zone) -> Zone:
    
    Super Class:
        Enum
    """
    
    def __new__(
            cls,
            color: GameColor,
            schema: Schema,
    ):
        obj = object.__new__(cls)
        obj._color = color
        obj._schema = schema
        return obj
    
    WHITE = (GameColor.WHITE, Schema.WHITE,)
    BLACK = (GameColor.BLACK, Schema.BLACK,)
    
    @property
    def color(self) -> GameColor:
        return self._color
    
    @property
    def schema(self) -> Schema:
        return self._schema

    
    @property
    def opposite(self) -> Zone:
        if self == Zone.WHITE:
            return Zone.BLACK
        return Zone.WHITE