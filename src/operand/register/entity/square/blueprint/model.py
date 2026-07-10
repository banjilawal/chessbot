# src/operand/register/entity/square/blueprint/operand.py

"""
Module: operand.register.entity.square.blueprint.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type, cast

from blueprint import SquareBlueprint
from err import SquareBlueprintNullException
from operand import EntityRegister


class SquareBlueprintEntityRegister(EntityRegister[SquareBlueprint]):
    """
    Role:
        -   Operand
        -   Data Holder

    Responsibilities:
        1.  Contains the operand and null_exception for an entity.

    Attributes:
        operand: SquareBlueprint
        null_exception: SquareBlueprintNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            operand: SquareBlueprint = Type[SquareBlueprint],
            null_exception: SquareBlueprintNullException = SquareBlueprintNullException(),
    ):
        """
        Args:
            operand: Operand
            null_exception: NullException
        """
        super().__init__(operand=operand, null_exception=null_exception)
        
    @property
    def operand(self) -> SquareBlueprint:
        return cast(SquareBlueprint, self.operand)
    
    @property
    def null_exception(self) -> SquareBlueprintNullException:
        return cast(SquareBlueprintNullException, self.null_exception)
    
    @property
    def is_square_blueprint_entity_register(self) -> bool:
        return isinstance(self, SquareBlueprintEntityRegister)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, SquareBlueprintEntityRegister):
            return (
                    self.operand == other.operand and
                    self.null_exception == other.null_exception
            )
    
