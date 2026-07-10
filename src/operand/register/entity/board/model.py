# src/operand/register/entity/operand.py

"""
Module: operand.register.entity.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Type, cast

from err import BoardNullException
from operand import EntityRegister, Board


class BoardEntityRegister(EntityRegister[Board]):
    """
    Role:
        -   Operand
        -   Data Holder

    Responsibilities:
        1.  Contains the operand and null_exception for an entity.

    Attributes:
        operand: Board
        null_exception: BoardNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            operand: Board = Type[Board],
            null_exception: BoardNullException = BoardNullException(),
    ):
        """
        Args:
            operand: Operand
            null_exception: NullException
        """
        super().__init__(operand=operand, null_exception=null_exception)
        
    @property
    def operand(self) -> Board:
        return cast(Board, self.a)
    
    @property
    def null_exception(self) -> BoardNullException:
        return cast(BoardNullException, self.null_exception)
    
    @property
    def board(self) -> Board:
        return self.operand
    
    @property
    def is_board_entity_register(self) -> bool:
        return isinstance(self, BoardEntityRegister)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, BoardEntityRegister):
            return (
                    self.operand == other.operand and
                    self.null_exception == other.null_exception
            )
    
