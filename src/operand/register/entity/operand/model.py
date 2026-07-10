# src/operand/register/entity/operand.py

"""
Module: operand.register.entity.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Type, cast

from err import VectorOperandRegisterNullException
from operand import EntityRegister, VectorOperandRegister


class VectorOperandEntityRegister(EntityRegister[VectorOperandRegister]):
    """
    Role:
        -   Operand
        -   Data Holder

    Responsibilities:
        1.  Contains the operand and null_exception for an entity.

    Attributes:
        operand: Operand
        null_exception: VectorOperandRegisterNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            operand: VectorOperandRegister = VectorOperandRegister,
            null_exception: VectorOperandRegisterNullException = VectorOperandRegisterNullException(),
    ):
        """
        Args:
            operand: Operand
            null_exception: NullException
        """
        super().__init__(operand=operand, null_exception=null_exception)
        
    @property
    def operand(self) -> VectorOperandRegister:
        return cast(VectorOperandRegister, self.a)
    
    @property
    def null_exception(self) -> VectorOperandRegisterNullException:
        return cast(VectorOperandRegisterNullException, self.null_exception)
    
    @property
    def operand(self) -> VectorOperandRegister:
        return self.operand
    
    @property
    def is_operand_entity_register(self) -> bool:
        return isinstance(self, VectorOperandEntityRegister)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, VectorOperandEntityRegister):
            return (
                    self.operand == other.operand and
                    self.null_exception == other.null_exception
            )
    
