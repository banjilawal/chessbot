# src/domain/metadata/blueprint/struct/node/vector/struct.py

"""
Module: domain.metadata.blueprint.struct.node.vector.struct
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Dict, Optional, Type, cast

from domain import NodeBlueprint, Vector, VectorNode
from err import VectorNodeNullException


class VectorNodeBlueprint(NodeBlueprint[VectorNode, Vector]):
    """
    Role:
        - Structural Wrapper

    Responsibilities:
        1.  Encapsulate a Vector payload with pointer references (next/previous) to
            enable doubly-linked traversal.
        2.  Provide type-safe accessors for payload inspection and node chaining.

    Attributes:
        payload: Optional[Vector]
        next: Optional[VectorNode]
        previous: Optional[VectorNode]
        
    Provides:

    Super Class:
        Node
    """
    
    def __init__(
            self,
            payload: Optional[Vector] | None = None,
            next: Optional[VectorNode] | None = None,
            previous: Optional[VectorNode] | None = None,
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
            payload=payload,
            next=next,
            previous=previous,
            domain_class=domain_class or VectorNode,
            domain_null_exception=domain_null_exception or VectorNodeNullException(),
        )
   
    @property
    def payload(self) -> Optional[Vector]:
        return cast(Vector, super().payload)
    
    @property
    def next(self) -> Optional[VectorNode]:
        return cast(VectorNode, super().next)
    
    @property
    def previous(self) -> Optional[VectorNode]:
        return cast(VectorNode, super().previous)
    
    @property
    def to_dict(self) -> Dict[str, Vector]:
        entry = {}
        if self.next is not None:
            next_node = self.next
            entry["next"] = next_node
        if self.previous is not None:
            previous_node = self.previous
            entry["previous"] = previous_node
        entry["payload"] = self.payload
        return entry
    
    @property
    def domain_class(self) -> Type[VectorNode]:
        return cast(Type[VectorNode], super().domain_class)
    
    @property
    def domain_null_exception(self) -> VectorNodeNullException:
        return cast(VectorNodeNullException, super().domain_null_exception)

    
    