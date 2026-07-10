# src/model/register/entity/team/blueprint/model.py

"""
Module: model.register.entity.team.blueprint.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type, cast

from blueprint import TeamBlueprint
from err import TeamBlueprintNullException
from model import EntityRegister


class TeamBlueprintEntityRegister(EntityRegister[TeamBlueprint]):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains the model and null_exception for an entity.

    Attributes:
        model: TeamBlueprint
        null_exception: TeamBlueprintNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            model: TeamBlueprint = Type[TeamBlueprint],
            null_exception: TeamBlueprintNullException = TeamBlueprintNullException(),
    ):
        """
        Args:
            model: Model
            null_exception: NullException
        """
        super().__init__(model=model, null_exception=null_exception)
        
    @property
    def model(self) -> TeamBlueprint:
        return cast(TeamBlueprint, self.model)
    
    @property
    def null_exception(self) -> TeamBlueprintNullException:
        return cast(TeamBlueprintNullException, self.null_exception)
    
    @property
    def is_team_blueprint_entity_register(self) -> bool:
        return isinstance(self, TeamBlueprintEntityRegister)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, TeamEntityRegister):
            return (
                    self.model == other.model and
                    self.null_exception == other.null_exception
            )
    
