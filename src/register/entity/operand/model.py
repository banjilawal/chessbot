# src/model/register/entity/model.py

"""
Module: model.register.entity.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Type, cast

from err import VectorOperandRegisterNullException
from model import EntityRegister, PointRegister


class VectorOperandEntityRegister(EntityRegister[PointRegister]):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains the model and null_exception for an entity.

    Attributes:
        model: Operand
        null_exception: VectorOperandRegisterNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            model: PointRegister = PointRegister,
            null_exception: VectorOperandRegisterNullException = VectorOperandRegisterNullException(),
    ):
        """
        Args:
            model: Model
            null_exception: NullException
        """
        super().__init__(model=model, null_exception=null_exception)
        
    @property
    def model(self) -> PointRegister:
        return cast(PointRegister, self.a)
    
    @property
    def null_exception(self) -> VectorOperandRegisterNullException:
        return cast(VectorOperandRegisterNullException, self.null_exception)
    
    @property
    def operand(self) -> PointRegister:
        return self.model
    
    @property
    def is_operand_entity_register(self) -> bool:
        return isinstance(self, VectorOperandEntityRegister)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, VectorOperandEntityRegister):
            return (
                    self.model == other.model and
                    self.null_exception == other.null_exception
            )
    
