# src/domain/metadata/blueprint/struct/binder/team.blueprint.py

"""
Module: domain.metadata.blueprint.struct.binder.team.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Dict, Optional, Type, cast

from domain import Archetype, BinderBlueprint, Team, TeamBinder
from err import TeamBinderNullException


class TeamBinderBlueprint(BinderBlueprint[TeamBinder, Team]):
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

     Provides:

     Super Class:
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
        Args:
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
        if self.white_team.archetype == Archetype.BLACK:
            return False
        if self.black_team.archetype == Archetype.WHITE:
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
    
    @property
    def domain_class(self) -> Type[TeamBinder]:
        return cast(Type[TeamBinder], super().domain_class)
    
    @property
    def domain_null_exception(self) -> TeamBinderNullException:
        return cast(TeamBinderNullException, super().domain_null_exception)
    

    
    
