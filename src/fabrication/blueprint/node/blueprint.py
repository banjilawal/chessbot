# src/blueprint/node/blueprint

"""
Module: blueprint.node.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Type, cast

from err import NodeNullException
from fabrication import Blueprint
from node import Node


class NodeBlueprint(Blueprint[Node]):
    """
     Role:
         -   DTO

     Responsibilities:
         1.  Provides values for instantiating a Node object

     Attributes:
         model_class: Type[Node]
         null_exception: Optional[NodeNullException]

     Provides:

     Super Class:
        Blueprint
     """
    
    def __init__(self, model_class: Type[Node], null_exception: NodeNullException,):
        """
        Args:
            model_class: Type[Node]
            null_exception: Optional[NodeModelNullException]
        """
        super().__init__(model_class=model_class, null_exception=null_exception)
        
    @property
    def model_class(self) -> Type[Node]:
        return cast(Type[Node], super()._model_class)
    
    @property
    def null_exception(self) -> NodeNullException:
        return cast(NodeNullException, super().null_exception)