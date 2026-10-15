# src/domain/metadata/blueprint/struct/node/blueprint.py

"""
Module: domain.metadata.blueprint.struct.node.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, Generic, Optional, Type, TypeVar, cast

from domain import Model, Node, StructBlueprint
from err import NodeNullException

T = TypeVar("T", bound="Node")
M = TypeVar("M", bound="Model")

class NodeBlueprint(StructBlueprint[T], ABC, Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a Node.

     Attributes:
         domain_class: Type[T]
         domain_null_exception: NodeNullException

     ProvideT:

     Super class:
        StructBlueprint
     """
    _payload: Optional[Any]
    _next: Optional[Node[Any]]
    _previouT: Optional[Node[Any]]
    
    def __init__(
            self,
            domain_class: Type[T],
            payload: Optional[Any] | None = None,
            next: Optional[Node[Any]] | None = None,
            previouT: Optional[Node[Any]] | None = None,
            domain_null_exception: Optional[NodeNullException] | None = None,
    ):
        """
        ArgT:
            domain_class: Type[T]
            payload: Optional[[Any]]
            next: Optional[Node[Any]]
            previouT: Optional[Node[Any]]
            domain_null_exception: Optional[NodeNullException]
        """
        super().__init__(
            domain_class=domain_class,
            domain_null_exception=domain_null_exception or NodeNullException()
        )
        self._payload = payload
        self._next = next
        self._previous = previous
    
    @property
    def payload(self) -> Optional[Any]:
        return self._payload
    
    @property
    def next(self) -> Optional[Node[Any]]:
        return self._next
    
    @property
    def previous(self) -> Optional[Node[Any]]:
        return self._previous
    
    @property
    def is_empty(self) -> bool:
        return (
                self._payload is None and
                self.does_not_have_orphan_pointers
        )
    
    @property
    def is_not_empty(self):
        return not self.is_empty
    
    @property
    def is_consistent(self) -> bool:
        return self.does_not_have_orphan_pointers
    
    @property
    def size(self) -> int:
        return len([self._payload]) + self.number_of_pointers
    
    @property
    def number_of_pointers(self) -> int:
        return len([self._next, self._previous])
    
    @property
    def has_orphan_pointers(self) -> bool:
        return self._payload is None and self.has_neighbors
    
    @property
    def does_not_have_orphan_pointers(self) -> bool:
        return not self.has_orphan_pointers
    
    @property
    def has_neighbors(self) -> bool:
        return self.number_of_pointers > 0
    
    @property
    def does_not_have_neighbors(self) -> bool:
        return not self.has_neighbors
    
    @property
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        pass
    
    @property
    def domain_class(self) -> Type[T]:
        return cast(Type[T], super().domain_class)
    
    @property
    def domain_null_exception(self) -> NodeNullException:
        return cast(NodeNullException, super().domain_null_exception)

    
    def __init__(
            self,

    ):
        """
        ArgT:
            payload: Optional[Any],
            next: Optional[Node[Any]]
            previouT: Optional[Node[Any]]
        """

    

    
    @next.setter
    def next(self, other: Node[Any]):
        self._next = other
    

    
    @previous.setter
    def previous(self, other: Node[Any]):
        self._previous = other
        


    
    
        
