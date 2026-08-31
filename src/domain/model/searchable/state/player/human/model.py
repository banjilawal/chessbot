# src/domain/model/searchable/state/player/human/model.py

"""
Module: domain.model.searchable.state.player.human.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from domain import Player
from game import GameAdviser


class HumanPlayer(Player):
    """
     Role:
         -  Data Holder

     Responsibilities:
        1.  Create, play, save, or terminate a Game.
        2.  Direct a Team's pieces that are in an Arena's Board.
        3.  Can seek advice on moves.
        4.  Can look up their previous games.

     Attributes:
         id: int
         name: str
         adviser: Optional[GameAdviser]

     Provides:

     Super Class:
        Player
     """
    
    def player(self, id: int, name: str, adviser: Optional[GameAdviser] | None = None, ):
        """
        Args:
            id: int
            name: str
            adviser: Optional[GameAdviser]
        """
        super().__init__(id=id, name=name, adviser=adviser)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, HumanPlayer):
            return self.id == other.id
        return False
