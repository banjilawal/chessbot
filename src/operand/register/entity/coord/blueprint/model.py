# src/operand/register/entity/coord/blueprint/operand.py

"""
Module: operand.register.entity.coord.blueprint.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type, cast

from blueprint import CoordBlueprint
from err import CoordBlueprintNullException
from operand import EntityRegister


class CoordBlueprintEntityRegister(EntityRegister[CoordBlueprint]):
    """
    Role:
        -   Operand
        -   Data Holder

    Responsibilities:
        1.  Contains the operand and null_exception for an entity.

    Attributes:
        operand: CoordBlueprint
        null_exception: CoordBlueprintNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            operand: CoordBlueprint = Type[CoordBlueprint],
            null_exception: CoordBlueprintNullException = CoordBlueprintNullException(),
    ):
        """
        Args:
            operand: Operand
            null_exception: NullException
        """
        super().__init__(operand=operand, null_exception=null_exception)
        
    @property
    def operand(self) -> CoordBlueprint:
        return cast(CoordBlueprint, self.operand)
    
    @property
    def null_exception(self) -> CoordBlueprintNullException:
        return cast(CoordBlueprintNullException, self.null_exception)
    
    @property
    def is_coord_blueprint_entity_register(self) -> bool:
        return isinstance(self, CoordBlueprintEntityRegister)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, CoordBlueprintEntityRegister):
            return (
                    self.operand == other.operand and
                    self.null_exception == other.null_exception
            )
    
