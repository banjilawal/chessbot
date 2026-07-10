# src/operand/register/entity/board/blueprint/operand.py

"""
Module: operand.register.entity.board.blueprint.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type, cast

from blueprint import BoardBlueprint
from err import BoardBlueprintNullException
from operand import EntityRegister


class BoardBlueprintEntityRegister(EntityRegister[BoardBlueprint]):
    """
    Role:
        -   Operand
        -   Data Holder

    Responsibilities:
        1.  Contains the operand and null_exception for an entity.

    Attributes:
        operand: BoardBlueprint
        null_exception: BoardBlueprintNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            operand: BoardBlueprint = Type[BoardBlueprint],
            null_exception: BoardBlueprintNullException = BoardBlueprintNullException(),
    ):
        """
        Args:
            operand: Operand
            null_exception: NullException
        """
        super().__init__(operand=operand, null_exception=null_exception)
        
    @property
    def operand(self) -> BoardBlueprint:
        return cast(BoardBlueprint, self.operand)
    
    @property
    def null_exception(self) -> BoardBlueprintNullException:
        return cast(BoardBlueprintNullException, self.null_exception)
    
    @property
    def is_board_blueprint_entity_register(self) -> bool:
        return isinstance(self, BoardBlueprintEntityRegister)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, BoardBlueprintEntityRegister):
            return (
                    self.operand == other.operand and
                    self.null_exception == other.null_exception
            )
    
