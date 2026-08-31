# src/domain/model/searchable/state/player/model.py

"""
Module: domain.model.searchable.state.player.model
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations

from abc import ABC
from typing import Optional

from domain import StateModel
from game import GameAdviser


class Player(StateModel, ABC):
    """
     Role:
         - Data Holder

     Responsibilities:
        2.  Direct a Team's pieces that are in an Arena's Board during a Game.

     Attributes:
         id: int
         name: str
         adviser: Optional[GameAdviser]

     Provides:

     Super Class:
        Model
     """
    _id: int
    _name: str
    _adviser: Optional[GameAdviser]
    
    def __init__(
            self,
            id: int,
            name: str,
            adviser: Optional[GameAdviser] | None = None,
    ):
        """
        Args:
            id: int
            name: str
            adviser: Optional[GameAdviser]
        """
        super().__init__(id=id)
        self._name = name
        self._adviser = adviser
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name: str):
        self._name = name
        
    @property
    def adviser(self) -> Optional[GameAdviser]:
        return self._adviser
    
    @adviser.setter
    def adviser(self, other: GameAdviser):
        self._adviser = other
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, Player):
            return self._id == other.id
        return False
    
    def __hash__(self):
        return hash(self._id)
