# src/domain/struct/binder/team/binder.py

"""
Module: domain.struct.binder.team.binder
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from __future__ import annotations

from typing import Dict, List

from config import GameColor
from domain import Archetype, ArchetypeBinder, Board, PlayerBinder, Team
from util import IdFactory


class TeamBinder(ArchetypeBinder[Team]):
    """
    Role:
        - Mapper

    Responsibility:
        1.  Use GameColor to map Team to Archetype.
        
    Attributes:
        white_team: Team
        black_team: Team
        to_dict: Dict[str, Team]
        
    Provides:
        
    Super Class:
       ArchetypeBinder
    """
    
    _entry: Dict[Archetype, Team]
    
    def __init__(
            self,
            board: Board,
            player_binder: PlayerBinder,
    ):
        """
        Args:
            board: Board,
            player_binder: PlayerBinder
        """
        super().__init__()
        for key in player_binder.to_dict.keys():
            archetype = player_binder[key].archetype
            team = Team(
                board=board,
                archetype=archetype,
                owner=player_binder[archetype],
                id=IdFactory.next_id(class_name="Team"),
            )
            self._entry[archetype] = team
    
    @property
    def white_team(self) -> Team:
        return self._entry[Archetype.WHITE]
    
    @property
    def black_team(self) -> Team:
        return self._entry[Archetype.BLACK]
    
    @property
    def teams(self) -> List[Team]:
        return [self.white_team, self.black_team]
    
    @property
    def entries_are_unique(self) -> bool:
        return self.is_full and self.white_team != self.black_team
    
    @property
    def entries_are_not_unique(self) -> bool:
        return self.is_full and self.white_team == self.black_team
    
    @property
    def consistency_exists(self) -> bool:
        if super().is_not_consistent:
            return False
        if self.entries_are_not_unique:
            return False
        if self.white_team.archetype != Archetype.WHITE:
            return False
        if self.black_team.archetype != Archetype.BLACK:
            return False
        return True
        
    @property
    def is_not_consistent(self) -> bool:
        return not self.consistency_exists
    
    @property
    def to_dict(self) -> Dict[str, Team]:
        return {
            "white": self.white_team,
            "black": self.black_team,
        }