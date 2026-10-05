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
        payload: Optional[Vector]
        next: Optional[Vector]
        Optional[Type[VectorNode]]
        domain_null_exception: Optional[VectorNodeNullException]

     Provides:

     Super Class:
        NodeBlueprint
     """
    _payload: Optional[Vector]
    _next: Optional[Vector]
    _previous: Optional[Vector]
    
    def __init__(
            self,
            payload: Optional[Vector] | None = None,
            next: Optional[Vector] | None = None,
            previous: Optional[Vector] | None = None,
            domain_class: Optional[Type[VectorNode]] | None = None,
            domain_null_exception: Optional[VectorNodeNullException] | None = None,
    ):
        """
        Args:
            payload: Optional[Vector]
            next: Optional[Vector]
            previous: Optional[Vector]
            Optional[Type[VectorNode]]
            domain_null_exception: Optional[VectorNodeNullException]
        """
        super().__init__(
            domain_class=domain_class or VectorNode,
            domain_null_exception=domain_null_exception or VectorNodeNullException(),
        )
        self._payload = payload
        self._next = next
        self._previous = previous
        
    @property
    def payload(self) -> Optional[Vector]:
        return self._payload
    
    @property
    def next(self) -> Optional[Vector]:
        return self._next
    
    @property
    def previous(self) -> Optional[Vector]:
        return self._previous
    
    @property
    def domain_class(self) -> Type[VectorNode]:
        return cast(Type[VectorNode], super().domain_class)
    
    @property
    def domain_null_exception(self) -> VectorNodeNullException:
        return cast(VectorNodeNullException, super().domain_null_exception)
    
    
