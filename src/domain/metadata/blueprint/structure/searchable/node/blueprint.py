# src/domain/metadata/blueprint/structure/node/blueprint

"""
Module: domain.metadata.blueprint.structure.node.blueprint.structure
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Type, TypeVar, cast

from domain import Blueprint, Node
from err import NodeNullException

T = TypeVar("T", bound="Node")


class NodeBlueprint(Blueprint[T], ABC, Generic[T]):
    """
     Role:
         -  DTO

     Responsibilities:
         1.  Provides values for instantiating a Node object

     Attributes:
         model_class: Type[Node]
         null_exception: Optional[NodeNullException]

     Provides:

     Super Class:
        Blueprint
     """
    
    def __init__(self, model_class: Type[T], null_exception: NodeNullException,):
        """
        Args:
            model_class: Type[Node]
            null_exception: Optional[NodeModelNullException]
        """
        super().__init__(model_class=model_class, null_exception=null_exception)
        
    @property
    def model_class(self) -> Type[T]:
        return cast(Type[T], super()._model_class)
    
    @property
    def null_exception(self) -> NodeNullException:
        return cast(NodeNullException, super().null_exception)