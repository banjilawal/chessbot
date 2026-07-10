# src/operand/register/entity/operand.py

"""
Module: operand.register.entity.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Type, cast

from err import ScalarNullException
from operand import EntityRegister, Scalar


class ScalarEntityRegister(EntityRegister[Scalar]):
    """
    Role:
        -   Operand
        -   Data Holder

    Responsibilities:
        1.  Contains the operand and null_exception for an entity.

    Attributes:
        operand: Scalar
        null_exception: ScalarNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            operand: Scalar = Type[Scalar],
            null_exception: ScalarNullException = ScalarNullException(),
    ):
        """
        Args:
            operand: Operand
            null_exception: NullException
        """
        super().__init__(operand=operand, null_exception=null_exception)
        
    @property
    def operand(self) -> Scalar:
        return cast(Scalar, self.a)
    
    @property
    def null_exception(self) -> ScalarNullException:
        return cast(ScalarNullException, self.null_exception)
    
    @property
    def scalar(self) -> Scalar:
        return self.operand
    
    @property
    def is_scalar_entity_register(self) -> bool:
        return isinstance(self, ScalarEntityRegister)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ScalarEntityRegister):
            return (
                    self.operand == other.operand and
                    self.null_exception == other.null_exception
            )
    
