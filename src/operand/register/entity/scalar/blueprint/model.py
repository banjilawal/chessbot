# src/operand/register/entity/scalar/blueprint/operand.py

"""
Module: operand.register.entity.scalar.blueprint.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type, cast

from blueprint import ScalarBlueprint
from err import ScalarBlueprintNullException
from operand import EntityRegister


class ScalarBlueprintEntityRegister(EntityRegister[ScalarBlueprint]):
    """
    Role:
        -   Operand
        -   Data Holder

    Responsibilities:
        1.  Contains the operand and null_exception for an entity.

    Attributes:
        operand: ScalarBlueprint
        null_exception: ScalarBlueprintNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            operand: ScalarBlueprint = Type[ScalarBlueprint],
            null_exception: ScalarBlueprintNullException = ScalarBlueprintNullException(),
    ):
        """
        Args:
            operand: Operand
            null_exception: NullException
        """
        super().__init__(operand=operand, null_exception=null_exception)
        
    @property
    def operand(self) -> ScalarBlueprint:
        return cast(ScalarBlueprint, self.operand)
    
    @property
    def null_exception(self) -> ScalarBlueprintNullException:
        return cast(ScalarBlueprintNullException, self.null_exception)
    
    @property
    def is_scalar_blueprint_entity_register(self) -> bool:
        return isinstance(self, ScalarBlueprintEntityRegister)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ScalarBlueprintEntityRegister):
            return (
                    self.operand == other.operand and
                    self.null_exception == other.null_exception
            )
    
