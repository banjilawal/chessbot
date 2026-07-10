# src/register/entity/operand/blueprint/py

"""
Module: register.entity.operand.blueprint.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from blueprint import PointRegisterBlueprint
from err import VectorOperandRegisterBlueprintNullException
from model import EntityRegister


class VectorOperandRegisterBlueprintEntityRegister(EntityRegister[PointRegisterBlueprint]):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains the model and null_exception for an entity.

    Attributes:
        model: VectorOperandRegisterBlueprint
        null_exception: VectorOperandRegisterBlueprintNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            model: PointRegisterBlueprint = PointRegisterBlueprint,
            null_exception: VectorOperandRegisterBlueprintNullException = VectorOperandRegisterBlueprintNullException(),
    ):
        """
        Args:
            model: Model
            null_exception: NullException
        """
        super().__init__(model=model, null_exception=null_exception)
        
    @property
    def model(self) -> PointRegisterBlueprint:
        return cast(PointRegisterBlueprint, self.model)
    
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
                    self.model == other.model and
                    self.null_exception == other.null_exception
            )
    
