# src/operand/register/entity/operand.py

"""
Module: operand.register.entity.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Type, cast

from err import SquareNullException
from operand import EntityRegister, Square


class SquareEntityRegister(EntityRegister[Square]):
    """
    Role:
        -   Operand
        -   Data Holder

    Responsibilities:
        1.  Contains the operand and null_exception for an entity.

    Attributes:
        operand: Square
        null_exception: SquareNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            operand: Square = Type[Square],
            null_exception: SquareNullException = SquareNullException(),
    ):
        """
        Args:
            operand: Operand
            null_exception: NullException
        """
        super().__init__(operand=operand, null_exception=null_exception)
        
    @property
    def operand(self) -> Square:
        return cast(Square, self.a)
    
    @property
    def null_exception(self) -> SquareNullException:
        return cast(SquareNullException, self.null_exception)
    
    @property
    def square(self) -> Square:
        return self.operand
    
    @property
    def is_square_entity_register(self) -> bool:
        return isinstance(self, SquareEntityRegister)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, SquareEntityRegister):
            return (
                    self.operand == other.operand and
                    self.null_exception == other.null_exception
            )
    
