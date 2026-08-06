# src/authorization/request/chain/remove/request.py

"""
Module: authorization.request.chain.remove.request
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Any, Dict, Generic, Optional, TypeVar, cast

from authorization import LinkedListRequest
from collection import LinkedList
from node import Node

T = TypeVar("T")


class LinkedListItemDeletionRequest(LinkedListRequest, ABC, Generic[T]):
    """
    Role:
        -  Request
        -  Data Transport
    
    Responsibilities:
        1. Provide information to get permission to run an operation.
    
    Attributes:
        id: int
    
    Provides:
    
    Super Class:
        Request
    """
    _node: Optional[Node[T]]
    _offset: Optional[int]
    
    def __init__(
            self,
            id: int,
            chain: LinkedList[T],
            node: Optional[Node[T]] | None = None,
            index: Optional[int] | None = None,
    ):
        """
        Args:
            id: int
            node: Node[T]
            chain: LinkedList[T]
            index: Optional[int]
        """
        super().__init__(id=id, chain=chain)
        self._node = node
        self._offset = index
        
    @property
    def chain(self) -> LinkedList[T]:
        return cast(LinkedList[T], super().chain)
    
    @property
    def node(self) -> Optional[Node[T]]:
        return self._node
    
    @property
    def offset(self) -> Optional[int]:
        return self._offset
    
    @property
    def is_remove_at_offset(self) -> bool:
        return (
                self._node is None and
                self._offset is not None and
                isinstance(self._offset, int)
        )
    
    @property
    def is_remove_by_node(self) -> bool:
        return (
                self._node is not None and
                self._offset is None and
                isinstance(self._node, Node)
        )
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "removal_offset": self._offset,
            "removal_node": self._node,
        }
    