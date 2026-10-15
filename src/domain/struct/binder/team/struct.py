# src/domain/struct/binder/team/binder.py

"""
Module: domain.struct.binder.team.binder
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from __future__ import annotations

from typing import Dict, List, cast

from domain import Account, Archetype, ArchetypeBinder, Game, Team


class TeamBinder(ArchetypeBinder[Team]):
    """
    Role:
        - Mapper

    Responsibility:
        1.  Immutable data structure insuring uniqueness and consistency
            between a Game's teams.
        
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
            white_team: Team,
            black_team: Team,
    ):
        """
        Args:
            white_team: Team
            black_team: Team
        """
        super().__init__(white_entry=white_team, black_entry=black_team)
        self._entry = {
            white_team.archetype: white_team,
            black_team.archetype: black_team,
        }
        
    @property
    def white_team(self) -> Team:
        return cast(Team, super().white_entry)
    
    @property
    def black_team(self) -> Team:
        return cast(Team, super().black_entry)
    
    @property
    def white_entry(self) -> Team:
        return self.white_entry
    
    @property
    def black_entry(self) -> Team:
        return self.black_entry
    
    @property
    def size(self) -> int:
        return len(self.bindings)
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def not_empty(self) -> bool:
        return not self.is_empty
    
    @property
    def archetypes_are_the_same(self) -> bool:
        return self.white_entry.archetype == self.black_entry.archetype
    
    @property
    def archetypes_differ(self) -> bool:
        return not self.archetypes_are_the_same
    
    @property
    def is_balanced(self) -> bool:
        return (
                self is not None and
                super().is_balanced and
                self.entries_are_unique and
                self.archetypes_differ
        )
    
    @property
    def is_not_balanced(self) -> bool:
        return not self.is_balanced
    
    @property
    def consistency_exists(self) -> bool:
        return (
                self.is_balanced and
                self.entries_are_unique and
                self._white_entry.archetype == Archetype.WHITE and
                self._black_entry.archetype == Archetype.BLACK
        )
    
    @property
    def is_not_consistent(self) -> bool:
        return not self.consistency_exists
    
    @property
    def entries_are_unique(self) -> bool:
        return (
                self.archetypes_differ and
                self.white_team != self.black_team
        )
    
    @property
    def entries_are_not_unique(self) -> bool:
        return not self.entries_are_unique
    
    @property
    def to_list(self) -> List[Team]:
        return [self.white_team, self.black_team]
    
    @property
    def bindings(self) -> Dict[Archetype, Team]:
        return self._entry
    
    @property
    def to_dict(self) -> Dict[str, Team]:
        return {
            "white": self.white_entry,
            "black": self.black_entry
        }
    