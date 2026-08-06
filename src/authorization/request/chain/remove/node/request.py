# src/authorization/request/chain/remove/node/request.py

"""
Module: authorization.request.chain.remove.node.request
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar, cast

from authorization import LinkedListItemDeletionRequest
from collection import LinkedList
from node import Node

T = TypeVar("T")


class NodeRemovalRequest(LinkedListItemDeletionRequest, ABC, Generic[T]):
    """
    Role:
        -  Request
        -  Data Transport
    
    Responsibilities:
        1. Provide information to get permission to run an operation.
    
    Attributes:
        id: int
        node: Node[T]
        chain: LinkedList[T]
        
    Provides:
    
    Super Class:
        LinkedListItemDeletionRequest
    """
    _node: Optional[Node[T]]
    
    def __init__(self, id: int, chain: LinkedList[T], node: Optional[Node[T]],):
        """
        Args:
            id: int
            node: Node[T]
            chain: LinkedList[T]
        """
        super().__init__(id=id, chain=chain)
        self._node = node
        
    @property
    def chain(self) -> LinkedList[T]:
        return cast(LinkedList[T], super().chain)
    
    @property
    def node(self) -> Optional[Node[T]]:
        return self._node
    