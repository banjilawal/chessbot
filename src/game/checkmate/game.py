# src/game/winner/report.py

"""
Module: game.winner.report
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from collection import CheckChain
from domain import Player, Team


class Checkmate:
    """
    Role:
        - Reporting

    Responsibilities:
        1.  Details about  the winner and their winner moves.
        
    Attributes:
        winner: Winner
        mmoves: CheckChain
        winner_has_right_team: bool
        winner_has_wrong_team: bool
        
    Provides:

    Super Class:
    """
    _winner: Player
    _winning_moves:  CheckChain
    
    def __init__(self, winner: Player, winning_moves: CheckChain, ):
        """
        Args:
            winner: Player
            winning_moves: CheckChain
        """
        self._winner = winner
        self._winning_moves = winning_moves
        
    @property
    def winner(self) -> Player:
        return self._winner
    
    @property
    def winning_moves(self) -> CheckChain:
        return self._winning_moves
    
    @property
    def player_owns_winning_team(self) -> bool:
        return self._winner == self._winning_moves.team.owner
    
    @property
    def player_does_not_own_winners(self) -> bool:
        return not self.player_owns_winning_team
    
    @property
    def winning_team(self) -> Team:
        return self.winning_moves.team
    
    