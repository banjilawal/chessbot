# src/model/register/entity/coord/blueprint/model.py

"""
Module: model.register.entity.coord.blueprint.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type, cast

from blueprint import CoordBlueprint
from err import CoordBlueprintNullException
from model import EntityRegister


class CoordBlueprintEntityRegister(EntityRegister[CoordBlueprint]):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains the model and null_exception for an entity.

    Attributes:
        model: CoordBlueprint
        null_exception: CoordBlueprintNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            model: CoordBlueprint = Type[CoordBlueprint],
            null_exception: CoordBlueprintNullException = CoordBlueprintNullException(),
    ):
        """
        Args:
            model: Model
            null_exception: NullException
        """
        super().__init__(model=model, null_exception=null_exception)
        
    @property
    def model(self) -> CoordBlueprint:
        return cast(CoordBlueprint, self.model)
    
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
                    self.model == other.model and
                    self.null_exception == other.null_exception
            )
    
