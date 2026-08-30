# src/domain/structure/register/player/structure.py

"""
Module: domain.structure.register.player.register
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Dict, List, cast

from domain import Player, Register


class Championship(Register[Player]):
    """
    Role:
        - Model
        -  Data Holder

    Responsibilities:
        1.  Contains the endpoints of a journey.

    Attributes:
        winner: Player
        looser: Player
        winner_is_looser: bool
        winner_is_not_looser: bool
            
    Provides:

    Super Class:
        Register
    """
    
    def __init__(self, winner: Player, looser: Player,):
        """
        Args:
            winner: Player
            looser: Player
        """
        super().__init__(a=winner, b=looser)
        
    @property
    def winner(self) -> Player:
        return cast(Player, super().a)
    
    @property
    def a(self) -> Player:
        return self.winner
    
    @property
    def looser(self) -> Player:
        return cast(Player, super().b)
    
    @property
    def b(self) -> Player:
        return self.looser

    @property
    def winner_same_as_looser(self) -> bool:
        return self.winner == self.looser
    
    @property
    def winner_differs_from_looser(self) -> bool:
        return not self.winner_same_as_looser
    
    @property
    def to_list(self) -> List[Player]:
        return [self.winner, self.looser]
    
    @property
    def to_dict(self) -> Dict[str, Player]:
        return {
            "winner": self.winner,
            "looser": self.looser,
        }
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, Championship):
            return (
                    self._winner == other.winner and
                    self._looser == other.looser
            )
    

    
