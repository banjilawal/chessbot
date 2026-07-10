# src/register/entity/node/blueprint/py

"""
Module: register.entity.node.blueprint.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type, cast

from blueprint import NodeBlueprint
from err import NodeBlueprintNullException
from model import EntityRegister


class NodeBlueprintEntityRegister(EntityRegister[NodeBlueprint]):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains the model and null_exception for an entity.

    Attributes:
        model: NodeBlueprint
        null_exception: NodeBlueprintNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            model: NodeBlueprint = Type[NodeBlueprint],
            null_exception: NodeBlueprintNullException = NodeBlueprintNullException(),
    ):
        """
        Args:
            model: Model
            null_exception: NullException
        """
        super().__init__(model=model, null_exception=null_exception)
        
    @property
    def model(self) -> NodeBlueprint:
        return cast(NodeBlueprint, self.model)
    
    @property
    def null_exception(self) -> NodeBlueprintNullException:
        return cast(NodeBlueprintNullException, self.null_exception)
    
    @property
    def is_node_blueprint_entity_register(self) -> bool:
        return isinstance(self, NodeBlueprintEntityRegister)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, NodeBlueprintEntityRegister):
            return (
                    self.model == other.model and
                    self.null_exception == other.null_exception
            )
    
