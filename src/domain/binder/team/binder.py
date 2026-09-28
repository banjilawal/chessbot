# src/domain/binder/team/binder.py

"""
Module: domain.binder.team.binder
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from __future__ import annotations

from typing import Dict, List

from config import GameColor
from domain import Archetype, ColorBinder, Team


class TeamColorBinder(ColorBinder[Team]):
    """
    Role:
        - Mapper

    Responsibility:
        1.  Use GameColor to map Team to Archetype.
        
    Attributes:
        white_team: Team
        black_team: Team
        
    Provides:
        teams_are_same: bool
        teams_differ: bool
        to_dict: Dict[GameColor, Dict[Archetype, Team]]
        
    Super Class:
       ColorBinder
    """
    _entry: Dict[GameColor, Dict[Archetype, Team]]
    
    def __init__(
            self,
            white_team: Team,
            black_team: Team,
    ):
        """
        Args:
            white_team: Team
            black_team: Team
        """
        super().__init__()
        self._entry = {
            GameColor.WHITE: {Archetype.WHITE: white_team},
            GameColor.BLACK: {Archetype.BLACK: black_team},
        }
    
    @property
    def white_team(self) -> Team:
        return self._entry[GameColor.WHITE][Archetype.WHITE]
    
    @property
    def black_team(self) -> Team:
        return self._entry[GameColor.BLACK][Archetype.BLACK]
    
    @property
    def teams(self) -> List[Team]:
        return [self.white_team, self.black_team]
    
    @property
    def teams_are_same(self) -> bool:
        return self.white_team == self.black_team
    
    @property
    def teams_differ(self) -> bool:
        return not self.teams_are_same
    
    @property
    def items_are_different(self) -> bool:
        return self.teams_differ
    
    @property
    def same_items(self) -> bool:
        return self.teams_are_same
    
    @property
    def to_dict(self) -> Dict[GameColor, Dict[Archetype, Team]]:
        return self._entry
        
    