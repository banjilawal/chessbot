# src/operand/register/entity/operand/blueprint/operand.py

"""
Module: operand.register.entity.operand.blueprint.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from blueprint import PointRegisterBlueprint
from err import VectorOperandRegisterBlueprintNullException
from operand import EntityRegister


class VectorOperandRegisterBlueprintEntityRegister(EntityRegister[PointRegisterBlueprint]):
    """
    Role:
        -   Operand
        -   Data Holder

    Responsibilities:
        1.  Contains the operand and null_exception for an entity.

    Attributes:
        operand: VectorOperandRegisterBlueprint
        null_exception: VectorOperandRegisterBlueprintNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            operand: PointRegisterBlueprint = PointRegisterBlueprint,
            null_exception: VectorOperandRegisterBlueprintNullException = VectorOperandRegisterBlueprintNullException(),
    ):
        """
        Args:
            operand: Operand
            null_exception: NullException
        """
        super().__init__(operand=operand, null_exception=null_exception)
        
    @property
    def operand(self) -> PointRegisterBlueprint:
        return cast(PointRegisterBlueprint, self.operand)
    
    @property
    def null_exception(self) -> VectorOperandRegisterBlueprintNullException:
        return cast(VectorOperandRegisterBlueprintNullException, self.null_exception)
    
    @property
    def is_operand_blueprint_entity_register(self) -> bool:
        return isinstance(self, VectorOperandRegisterBlueprintEntityRegister)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, PointRegisterBlueprint):
            return (
                    self.operand == other.operand and
                    self.null_exception == other.null_exception
            )
    
