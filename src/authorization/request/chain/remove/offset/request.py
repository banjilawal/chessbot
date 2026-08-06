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

from authorization import LinkedListItemDeletionRequest
from collection import LinkedList



class OffsetRemovalRequest(LinkedListItemDeletionRequest):
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
    _offset: int
    
    def __init__(
            self,
            id: int,
            offset: int,
            chain: LinkedList[T],
    ):
        """
        Args:
            id: int
            offset: int
            chain: LinkedList[T]
        """
        super().__init__(id=id, chain=chain)
        self._offset = offset
        
    @property
    def chain(self) -> LinkedList[T]:
        return cast(LinkedList[T], super().chain)
    
    @property
    def offset(self) -> int:
        return self._offset
    
    @property
    def is_tail_offset(self) -> bool:
        return self._offset < 0
    
    @property
    def is_head_offset(self) -> bool:
        return self._offset >=0
    