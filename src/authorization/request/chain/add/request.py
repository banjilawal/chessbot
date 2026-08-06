# src/authorization/request/chain/add/request.py

"""
Module: authorization.request.chain.add.request
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar, cast

from authorization import LinkedListRequest
from collection import LinkedList
from node import Node

T = TypeVar("T")


class AddNodeRequest(LinkedListRequest, ABC, Generic[T]):
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
    _node: Node[T]
    _index: Optional[int]
    
    def __init__(
            self,
            id: int,
            node: Node[T],
            chain: LinkedList[T],
            index: Optional[int] | None = None
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
        self._index = index
        
    @property
    def chain(self) -> LinkedList[T]:
        return cast(LinkedList[T], super().chain)
    
    @property
    def node(self) -> Node[T]:
        return self._node
    
    @property
    def index(self) -> Optional[int]:
        return self._index
    