# src/domain/model/searchable/state/player/machine/model.py

"""
Module: domain.model.searchable.state.player.machine.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain import Player
from game import GameAdviser


class MachinePlayer(Player):
    """
     Role:
         -  Data Holder

     Responsibilities:
        1.  Machine player can only execute GameAdviser recommendations about moves.

     Attributes:
         id: int
         name: str
         adviser: GameAdviser

     Provides:

     Super Class:
        Player
     """
    
    def __init__(self, id: int, name: str, adviser: GameAdviser):
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
        if isinstance(other, MachinePlayer):
            return self.id == other.id
        return False
