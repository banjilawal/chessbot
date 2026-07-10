# src/operand/register/entity/team/blueprint/operand.py

"""
Module: operand.register.entity.team.blueprint.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type, cast

from blueprint import TeamBlueprint
from err import TeamBlueprintNullException
from operand import EntityRegister


class TeamBlueprintEntityRegister(EntityRegister[TeamBlueprint]):
    """
    Role:
        -   Operand
        -   Data Holder

    Responsibilities:
        1.  Contains the operand and null_exception for an entity.

    Attributes:
        operand: TeamBlueprint
        null_exception: TeamBlueprintNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            operand: TeamBlueprint = Type[TeamBlueprint],
            null_exception: TeamBlueprintNullException = TeamBlueprintNullException(),
    ):
        """
        Args:
            operand: Operand
            null_exception: NullException
        """
        super().__init__(operand=operand, null_exception=null_exception)
        
    @property
    def operand(self) -> TeamBlueprint:
        return cast(TeamBlueprint, self.operand)
    
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
                    self.operand == other.operand and
                    self.null_exception == other.null_exception
            )
    
