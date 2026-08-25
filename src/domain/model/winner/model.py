# src/domain/model/winner/model.py

"""
Module: domain.model.winner.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain import DataModelObject, Player, Team


class GameWinner(DataModelObject):
    _champion: Player
    _team: Team
    _loss: int
    _prize: int
    _total_score: int
    
    def __init__(self,
            champion: Player,
            team: Team,
            loss: int,
            prize: int,
    ):
        """
        Args:
            champion: Player
            team: Team
            loss: int
            prize: int
        """
        self._champion = champion
        self._team = team
        self._loss = loss
        self._prize = prize
        self._total_score = self._prize - self._loss
        
    @property
    def champion(self) -> Player:
        return self._champion
    
    @property
    def team(self) -> Team:
        return self._team
    
    @property
    def loss(self) -> int:
        return self._loss
    
    @property
    def prize(self) -> int:
        return self._prize
    
    @property
    def total_score(self) -> int:
        return self._total_score