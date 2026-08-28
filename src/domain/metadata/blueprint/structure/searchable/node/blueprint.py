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
         1.  Provides values for hydrating a Node object

     Attributes:
         domain_class: Type[T]
         domain_null_exception: Optional[NodeNullException]

     Provides:

     Super Class:
        Blueprint
     """
    
    def __init__(self, domain_class: Type[T], domain_null_exception: NodeNullException, ):
        """
        Args:
            domain_class: Type[Node]
            domain_null_exception: Optional[NodeModelNullException]
        """
        super().__init__(domain_class=domain_class, domain_null_exception=domain_null_exception)
        
    @property
    def domain_class(self) -> Type[T]:
        return cast(Type[T], super()._domain_class)
    
    @property
    def domain_null_exception(self) -> NodeNullException:
        return cast(NodeNullException, super().domain_null_exception)