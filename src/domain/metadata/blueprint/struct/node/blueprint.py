# src/domain/metadata/blueprint/struct/node/blueprint.py

"""
Module: domain.metadata.blueprint.struct.node.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Type, TypeVar, cast

from domain import Node, StructBlueprint
from err import NodeNullException


T = TypeVar("T", bound="Node")

class NodeBlueprint(StructBlueprint[T], ABC, Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a Node.

     Attributes:
         domain_class: Type[T]
         domain_null_exception: NodeNullException

     Provides:

     Super Class:
        Blueprint
     """
    
    def __init__(
            self,
            domain_class: Type[T],
            domain_null_exception: NodeNullException,
    ):
        """
        Args:
            domain_class: Type[T]
            domain_null_exception: NodeNullException
        """
        super().__init__(
            domain_class=domain_class,
            domain_null_exception=domain_null_exception
        )
    
    @property
    def domain_class(self) -> Type[T]:
        return cast(Type[T], super().domain_class)
    
    @property
    def domain_null_exception(self) -> NodeNullException:
        return cast(NodeNullException, super().domain_null_exception)
    
    
