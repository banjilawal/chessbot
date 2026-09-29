# src/domain/model/searchable/encounter/checkmate/model.py.py

"""
Module: domain.model.searchable.encounter.checkmate.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from typing import Dict, Optional, cast

from config import GameColor
from domain import KingToken, Encounter, Maneuver, Player, Square, Token


class CheckmateEncounter(Encounter):
    """
    Role:
        - Model
        - Data Holder

    Responsibilities:
        1.  Details about an encounter.

    Attributes:
        id: int
        victim: KingToken
        maneuver: Maneuver
        location: Square
        attacker_reward: int

    Provides:
        
    Super Class:
        Encounter
    """

    
    def __init__(
            self,
            id: int,
            counter_maneuver: KingToken,
            attacker_maneuver: Maneuver,
            location: Optional[Square] | None = None,
            attacker_reward: Optional[int] | None = None,
    ):
        """
        Args:
            id: int
            counter_maneuver: KingToken
            attacker_maneuver: Maneuver
            location: Optional[Square]
            attacker_reward: Optional[int]
        """
        super().__init__(
            id=id,
            counter_maneuver=counter_maneuver,
            attacker_maneuver=attacker_maneuver,
            location=location,
            attacker_reward=attacker_reward,
        )
        
    @property
    def looser(self) -> KingToken:
        return cast(KingToken, super().victim)
    
    @property
    def victim(self) -> KingToken:
        return self.looser
    
    @property
    def victor(self) -> Token:
        return self.initiater
    
    @property
    def winner(self) -> Dict[str, Dict[GameColor, Player]]:
        
        table: Dict[str, Dict[GameColor, Player]]
        player = self.victor.team.owner
        color = self._encounter.victor.team.archetype.color
   
        
        winning_team = self._encounter.victor.team
        winning_archetype = winning_team.archetyp
        winner = winning_team.owner
        archetype.
        
        
        winner_archetype = winner_team.archetype
        if winner_archety
        
        team_binder = self._encounter.victor.team.board.team_binder
        player_binder = self._encount.victim.team.board.arena.player_binder
        
        winner_archetype = sel
        
        return {color:}
        self._encounter.victor.team.owner
    
    @

    def __eq__(self, other) -> bool:
        if other is None:
            return False
        if other == self:
            return True
        if isinstance(other, CheckmateEncounter):
            return self.id == other.id
        return False
    


        
        
        
    