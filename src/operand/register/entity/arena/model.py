# src/operand/register/entity/operand.py

"""
Module: operand.register.entity.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Type, cast

from err import ArenaNullException
from operand import EntityRegister, Arena


class ArenaEntityRegister(EntityRegister[Arena]):
    """
    Role:
        -   Operand
        -   Data Holder

    Responsibilities:
        1.  Contains the operand and null_exception for an entity.

    Attributes:
        operand: Arena
        null_exception: ArenaNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            operand: Arena = Type[Arena],
            null_exception: ArenaNullException = ArenaNullException(),
    ):
        """
        Args:
            operand: Operand
            null_exception: NullException
        """
        super().__init__(operand=operand, null_exception=null_exception)
        
    @property
    def operand(self) -> Arena:
        return cast(Arena, self.a)
    
    @property
    def null_exception(self) -> ArenaNullException:
        return cast(ArenaNullException, self.null_exception)
    
    @property
    def arena(self) -> Arena:
        return self.operand
    
    @property
    def is_arena_entity_register(self) -> bool:
        return isinstance(self, ArenaEntityRegister)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ArenaEntityRegister):
            return (
                    self.operand == other.operand and
                    self.null_exception == other.null_exception
            )
    
