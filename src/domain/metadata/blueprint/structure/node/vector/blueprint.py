# src/domain/metadata/blueprint/structure/node/vector/blueprint.py

"""
Module: domain.metadata.blueprint.structure.node.vector.blueprint.structure
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from err import VectorNodeNullException
from fabrication import NodeBlueprint
from domain.model import Vector
from domain.structure.node import VectorNode


class VectorNodeBlueprint(NodeBlueprint[Vector]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provides values for hydrating a VectorNode object

     Attributes:
        vector: Vector
        domain_class: Type[VectorNode]
        domain_null_exception: Optional[VectorNodeNullException]

     Provides:

     Super Class:
        NodeBlueprint
     """
    _vector: VectorBlueprint
    
    def __init__(
            self,
            vector: Vector,
            domain_class: Type[VectorNode] = VectorNode,
            domain_null_exception: Optional[VectorNodeNullException] | None = None,
    ):
        """
        Args:
            vector: Vector
            domain_class: Type[VectorNode]
            domain_null_exception: Optional[VectorNodeNullException]
        """
        super().__init__(domain_class=domain_class, domain_null_exception=domain_null_exception or VectorNodeNullException())
        self._vector = vector
        
    @property
    def vector(self) -> Vector:
        return self._vector
 
    @property
    def domain_class(self) -> Type[VectorNode]:
        return cast(Type[VectorNode], super().domain_class)
    
    @property
    def domain_null_exception(self) -> VectorNodeNullException:
        return cast(VectorNodeNullException, super().domain_null_exception)