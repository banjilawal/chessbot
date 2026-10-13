# src/domain/struct/binder/team/binder.py

"""
Module: domain.struct.binder.team.binder
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from __future__ import annotations

from typing import Dict, List, cast

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
            white_entry: Team,
            black_entry: Team,
    ):
        """
        Args:
            board: Board,
            player_binder: PlayerBinder
        """
        super().__init__(white_entry=white_entry, black_entry=black_entry)
        self._entry[white_entry.archetype] = white_entry
        
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
        return cast(Team, super().white_entry)
    
    @property
    def black_team(self) -> Team:
        return cast(Team, super().black_entry)
    
    @property
    def teams(self) -> List[Team]:
        return [self.white_team, self.black_team]
    
    @property
    def white_entry(self) -> Team:
        return self._white_entry
    
    @property
    def black_entry(self) -> Team:
        return self._black_entry
    
    @property
    def archetypes_are_the_same(self) -> bool:
        return not self.archetypes_differ
    
    @property
    def archetypes_differ(self) -> bool:
        return self._white_entry.archetype != self._black_entry.archetype
    
    @property
    def is_balanced(self) -> bool:
        return (
                self is not None and
                super().is_balanced and
                self.entries_are_unique and
                self.archetypes_differ
        )
    
    @property
    @abstractmethod
    def is_not_balanced(self) -> bool:
        return not self.is_balanced
    
    @property
    def consistency_exists(self) -> bool:
        return self.is_balanced
    
    @property
    def is_not_consistent(self) -> bool:
        return not self.consistency_exists
    
    @property
    def entries_are_unique(self) -> bool:
        return self.is_full and self.white_team != self.black_team
    
    @property
    def entries_are_not_unique(self) -> bool:
        return self.is_full and self.white_team == self.black_team
    
    @property
    @abstractmethod
    def bindings(self) -> Dict[Archetype, T]:
        pass
    
    @property
    def to_dict(self) -> Dict[str, T]:
        return {
            "white": self._white_entry,
            "black": self._black_entry
        }
    

    
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