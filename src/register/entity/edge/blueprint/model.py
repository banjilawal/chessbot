# src/register/entity/edge/blueprint/py

"""
Module: register.entity.edge.blueprint.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type, cast

from blueprint import EdgeBlueprint
from err import EdgeBlueprintNullException
from model import EntityRegister


class EdgeBlueprintEntityRegister(EntityRegister[EdgeBlueprint]):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains the model and null_exception for an entity.

    Attributes:
        model: EdgeBlueprint
        null_exception: EdgeBlueprintNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            model: EdgeBlueprint = Type[EdgeBlueprint],
            null_exception: EdgeBlueprintNullException = EdgeBlueprintNullException(),
    ):
        """
        Args:
            model: Model
            null_exception: NullException
        """
        super().__init__(model=model, null_exception=null_exception)
        
    @property
    def model(self) -> EdgeBlueprint:
        return cast(EdgeBlueprint, self.model)
    
    @property
    def null_exception(self) -> EdgeBlueprintNullException:
        return cast(EdgeBlueprintNullException, self.null_exception)
    
    @property
    def is_edge_blueprint_entity_register(self) -> bool:
        return isinstance(self, EdgeBlueprintEntityRegister)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, EdgeBlueprintEntityRegister):
            return (
                    self.model == other.model and
                    self.null_exception == other.null_exception
            )
    
