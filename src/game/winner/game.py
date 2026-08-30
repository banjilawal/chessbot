# src/game/winner/report.py

"""
Module: game.winner.report
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain import Championship, Player, Team
from game import Checkmate


class GameWin:
    """
    Role:
        - Reporting

    Responsibilities:
        1.  Details about  the winner and their checkmate moves.
        
    Attributes:
        checkmate: Checkmate
        championship: Championship
        winner_has_right_team: bool
        winner_has_wrong_team: bool
        
    Provides:

    Super Class:
    """
    _checkmate: Checkmate
    _championship: Championship
    
    def __init__(
            self,
            checkmate: Checkmate,
            championship: Championship,
    ):
        """
        Args:
            checkmate: Checkmate
            championship: Championship
        """
        self._checkmate = checkmate
        self._championship = championship
        
    @property
    def checkmate(self) -> Checkmate:
        return self._checkmate
    
    @property
    def championship(self) -> Championship:
        return self._championship
    
    @property
    def winner(self) -> Player:
        if self.winner_has_right_team:
            return self._championship.winner
        return self._checkmate.winner
    
    @property
    def winner_has_right_team(self) -> bool:
        return self._championship.winner == self._checkmate.winner
    
    @property
    def winner_has_wrong_team(self) -> bool:
        return not self.winner_has_right_team
    
    @property
    def winning_team(self) -> Team:
        return self.checkmate.attacker.team.owner
    
    @property
    def loosing_team(self) -> Team:
        return self._checkmate.mated_king.team
    
    @property
    def looser_has_right_team(self) -> bool:
        return self._championship.looser == self.loosing_team.owner
    