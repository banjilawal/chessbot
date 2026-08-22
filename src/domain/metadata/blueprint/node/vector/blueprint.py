# src/domain/metadata/blueprint/node/vector/blueprint.py

"""
Module: domain.metadata.blueprint.node.vector.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from err import VectorNodeNullException
from fabrication import NodeBlueprint
from domain.model import Vector
from domain.structures.node import VectorNode


class VectorNodeBlueprint(NodeBlueprint):
    """
     Role:
         -   DTO

     Responsibilities:
         1.  Provides values for instantiating a VectorNode object

     Attributes:
        vector: Vector
        model_class: Type[VectorNode]
        null_exception: Optional[VectorNodeNullException]

     Provides:

     Super Class:
        NodeBlueprint
     """
    _vector: Vector
    
    def __init__(
            self,
            vector: Vector,
            model_class: Type[VectorNode] = VectorNode,
            null_exception: Optional[VectorNodeNullException] | None = None,
    ):
        """
        Args:
            vector: Vector
            model_class: Type[VectorNode]
            null_exception: Optional[VectorNodeNullException]
        """
        super().__init__(model_class=model_class, null_exception=null_exception or VectorNodeNullException())
        self._vector = vector
        
    @property
    def vector(self) -> Vector:
        return self._vector
 
    @property
    def model_class(self) -> Type[VectorNode]:
        return cast(Type[VectorNode], super().model_class)
    
    @property
    def null_exception(self) -> VectorNodeNullException:
        return cast(VectorNodeNullException, super().null_exception)