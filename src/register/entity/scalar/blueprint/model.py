# src/register/entity/scalar/blueprint/py

"""
Module: register.entity.scalar.blueprint.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type, cast

from blueprint import ScalarBlueprint
from err import ScalarBlueprintNullException
from model import EntityRegister


class ScalarBlueprintEntityRegister(EntityRegister[ScalarBlueprint]):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains the model and null_exception for an entity.

    Attributes:
        model: ScalarBlueprint
        null_exception: ScalarBlueprintNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            model: ScalarBlueprint = Type[ScalarBlueprint],
            null_exception: ScalarBlueprintNullException = ScalarBlueprintNullException(),
    ):
        """
        Args:
            model: Model
            null_exception: NullException
        """
        super().__init__(model=model, null_exception=null_exception)
        
    @property
    def model(self) -> ScalarBlueprint:
        return cast(ScalarBlueprint, self.model)
    
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
                    self.model == other.model and
                    self.null_exception == other.null_exception
            )
    
