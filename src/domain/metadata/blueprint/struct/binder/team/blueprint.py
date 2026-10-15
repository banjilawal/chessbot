# src/domain/metadata/blueprint/struct/binder/team.blueprint.py

"""
Module: domain.metadata.blueprint.struct.binder.team.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Dict, List, Optional, Type

from domain import Archetype, BinderBlueprint, Team, TeamBinder
from err import TeamBinderNullException


class TeamBinderBlueprint(BinderBlueprint[TeamBinder]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a TeamBinder.

     Attributes:
        white_team: Team
        black_team: Team
        domain_class: Optional[Type[TeamBinder]]
        domain_null_exception: Optional[TeamBinderNullException]

     ProvideT:

     Super class:
        BinderBlueprint
     """
    
    _white_team: Team
    _black_team: Team
    
    def __init__(
            self,
            white_team: Team,
            black_team: Team,
            domain_class: Optional[Type[TeamBinder]] | None = None,
            domain_null_exception: Optional[TeamBinderNullException] | None = None,
    ):
        """
        ArgT:
            white_team: Team
            black_team: Team
            domain_class: Optional[Type[TeamBinder]]
            domain_null_exception: Optional[TeamBinderNullException]
        """
        super().__init__(
            domain_class=domain_class or TeamBinder,
            domain_null_exception=domain_null_exception or TeamBinderNullException(),
        )
        self._white_team = white_team
        self._black_team = black_team
        
    @property
    def white_team(self) -> Team:
        return self._white_team
    
    @property
    def black_team(self) -> Team:
        return self._black_team
    
    @property
    def teams_are_unique(self) -> bool:
        return self._white_team != self._black_team
    
    @property
    def teams_are_not_unique(self) -> bool:
        return not self.teams_are_unique
    
    @property
    def entries_are_unique(self) -> bool:
        return self.teams_are_unique
    
    @property
    def entries_are_not_unique(self) -> bool:
        return not self.entries_are_unique
    
    @property
    def archetypes_are_the_same(self) -> bool:
        return self._white_team.archetype == self._black_team.archetype
    
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
                self._white_team.archetype == Archetype.WHITE and
                self._black_team.archetype == Archetype.BLACK
        )
    
    @property
    def is_not_consistent(self) -> bool:
        return not self.consistency_exists
    
    @property
    def bindings(self) -> Dict[Archetype, Team]:
        return {
            self._white_team.archetype: self._white_team,
            self._black_team.archetype: self._black_team,
        }
    
    @property
    def to_list(self) -> List[Team]:
        return [self._white_team, self._black_team]
    
    @property
    def to_dict(self) -> Dict[str, Team]:
        return {
            "white": self._white_team,
            "black": self._black_team,
        }
    