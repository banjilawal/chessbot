# src/model/register/entity/model.py

"""
Module: model.register.entity.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Type, cast

from err import TeamNullException
from model import EntityRegister, Team


class TeamEntityRegister(EntityRegister[Team]):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains the model and null_exception for an entity.

    Attributes:
        model: Team
        null_exception: TeamNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(self, model: Team = Type[Team], null_exception: TeamNullException = TeamNullException(),):
        """
        Args:
            model: Model
            null_exception: NullException
        """
        super().__init__(model=model, null_exception=null_exception)
        
    @property
    def model(self) -> Team:
        return cast(Team, self.a)
    
    @property
    def null_exception(self) -> TeamNullException:
        return cast(TeamNullException, self.null_exception)
    
    @property
    def team(self) -> Team:
        return self.model
    
    @property
    def is_team_entity_register(self) -> bool:
        return isinstance(self, TeamEntityRegister)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, TeamEntityRegister):
            return (
                    self.model == other.model and
                    self.null_exception == other.null_exception
            )
    
