# src/operand/register/entity/operand.py

"""
Module: operand.register.entity.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Type, cast

from err import TeamNullException
from operand import EntityRegister, Team


class TeamEntityRegister(EntityRegister[Team]):
    """
    Role:
        -   Operand
        -   Data Holder

    Responsibilities:
        1.  Contains the operand and null_exception for an entity.

    Attributes:
        operand: Team
        null_exception: TeamNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(self, operand: Team = Type[Team], null_exception: TeamNullException = TeamNullException(),):
        """
        Args:
            operand: Operand
            null_exception: NullException
        """
        super().__init__(operand=operand, null_exception=null_exception)
        
    @property
    def operand(self) -> Team:
        return cast(Team, self.a)
    
    @property
    def null_exception(self) -> TeamNullException:
        return cast(TeamNullException, self.null_exception)
    
    @property
    def team(self) -> Team:
        return self.operand
    
    @property
    def is_team_entity_register(self) -> bool:
        return isinstance(self, TeamEntityRegister)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, TeamEntityRegister):
            return (
                    self.operand == other.operand and
                    self.null_exception == other.null_exception
            )
    
