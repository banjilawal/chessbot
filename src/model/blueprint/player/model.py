# src/model/blueprint/player/model.py

"""
Module: model.blueprint.player.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from logic.engine import Engine
from model import Blueprint, Player


class PlayerBlueprint(Blueprint[Player]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides values for instantiating a Player object.

    Attributes:
        id: int
        name: str
        engine: Engine
            
    Provides:

     Super Class:
        Blueprint
     """
    _id: Optional[int]
    _name: Optional[str]
    _engine: Optional[Engine]
    
    def __init__(
            self,
            id: Optional[int] | None = None,
            name: Optional[str] | None = None,
            engine: Optional[Engine] | None = None,
    ):
        """
        Args:
            id: int
            name: str
            engine: Engine
        """
        super().__init__()
        self._id = id
        self._name = name
        self._engine = engine

    @property
    def id(self) -> Optional[int]:
        return self._id
    
    @property
    def name(self) -> Optional[str]:
        return self._name
    
    @property
    def engine(self) -> Optional[Engine]:
        return self._engine