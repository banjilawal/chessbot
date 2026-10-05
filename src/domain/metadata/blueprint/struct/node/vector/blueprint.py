# src/domain/metadata/blueprint/struct/node/vector.blueprint.py

"""
Module: domain.metadata.blueprint.struct.node.vector.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import Vector, NodeBlueprint, VectorNode
from err import VectorNodeNullException


class VectorNodeBlueprint(NodeBlueprint[VectorNode]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a VectorNode.

     Attributes:
        position: Optional[Vector]
        previous_position: Optional[Vector]
        Optional[Type[VectorNode]]
        domain_null_exception: Optional[VectorNodeNullException]

     Provides:

     Super Class:
        NodeBlueprint
     """
    _position: Optional[Vector]
    _previous_position: Optional[Vector]
    
    def __init__(
            self,
            position: Optional[Vector] | None = None,
            previous_position: Optional[Vector] | None = None,
            domain_class: Optional[Type[VectorNode]] | None = None,
            domain_null_exception: Optional[VectorNodeNullException] | None = None,
    ):
        """
        Args:
            position: Optional[Vector]
            previous_position: Optional[Vector]
            Optional[Type[VectorNode]]
            domain_null_exception: Optional[VectorNodeNullException]
        """
        super().__init__(
            domain_class=domain_class or VectorNode,
            domain_null_exception=domain_null_exception or VectorNodeNullException(),
        )
        self._position = position
        self._previous_position = previous_position
        
    @property
    def position(self) -> Optional[Vector]:
        return self._position
    
    @property
    def previous_position(self) -> Optional[Vector]:
        return self._previous_position
    
    @property
    def domain_class(self) -> Type[VectorNode]:
        return cast(Type[VectorNode], super().domain_class)
    
    @property
    def domain_null_exception(self) -> VectorNodeNullException:
        return cast(VectorNodeNullException, super().domain_null_exception)
    
    
