# src/domain/model/searchable/state/player/model.py

"""
Module: domain.model.searchable.state.player.model
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations


from typing import Optional

from domain import Account, Archetype, Game, StateModel
from sync import GameAdviser


class Player(StateModel):
    """
     Role:
         - Data Holder

     Responsibilities:
        2.  Direct a Team's pieces that are in an Arena's Board during a Game.

     Attributes:
        id: int
        game: Game
        account: Account,
        archetype: Archetype,
        adviser: Optional[GameAdviser]

     Provides:

     Super Class:
        Model
     """
    _id: int
    _game: Game
    _account: Account
    _archetype: Archetype
    _adviser: Optional[GameAdviser]
    
    def __init__(
            self,
            id: int,
            game: Game,
            account: Account,
            archetype: Archetype,
            adviser: Optional[GameAdviser] | None = None,
    ):
        """
        Args:
            id: int
            game: Game
            account: Account,
            archetype: Archetype,
            adviser: Optional[GameAdviser]
        """
        super().__init__(id=id)
        self._game = game
        self._account = account
        self._archetype = archetype
        self._adviser = adviser
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def account(self) -> Account:
        return self._account
    
    @property
    def archetype(self) -> Archetype:
        return self._archetype
    
    @property
    def game(self) -> Game:
        return self._game
        
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
