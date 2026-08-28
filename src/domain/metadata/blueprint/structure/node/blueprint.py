# src/domain/metadata/blueprint/structure/node/blueprint

"""
Module: domain.metadata.blueprint.structure.node.structure
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Type, TypeVar, cast

from domain import Node, StructureBlueprint
from domain import SearchableModelBlueprint
from err import NodeNullException

T = TypeVar("T", bound="SearchableModelBlueprint")

class NodeBlueprint(StructureBlueprint[Node], ABC, Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provides values for hydrating a Node object.

     Attributes:
        domain_class: Type[Node]
        domain_null_exception: NodeNullException
        payload_blueprint: T

     Provides:

     Super Class:
        StructureBlueprint
     """
    _payload_blueprint: T
    
    def __init__(
            self, 
            domain_class: Type[Node],
            domain_null_exception: NodeNullException,
            payload_blueprint: T,
            
    ):
        """
        Args:
            domain_class: Type[Node]
            domain_null_exception: NodeNullException
            payload_blueprint: T
        """
        super().__init__(
            domain_class=domain_class,
            domain_null_exception=domain_null_exception
        )
        self._paylod_blueprint = payload_blueprint
        
    @property
    def domain_class(self) -> Type[T]:
        return cast(Type[T], super()._domain_class)
    
    @property
    def domain_null_exception(self) -> NodeNullException:
        return cast(NodeNullException, super().domain_null_exception)
    
    @property
    def payload_blueprint(self) -> T:
        return self._paylod_blueprint