# src/authorization/request/chain/request.py

"""
Module: authorization.request.chain.request
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from authorization import Request


T = TypeVar("T", bound="LikedList")


class LinkedListRequest(Request, ABC, Generic[T]):
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
    chain: T
    
    def __init__(self, id: int, chain: T, ):
        """
        Args:
            id: int
            chain: T
        """
        super().__init__(id=id)
        self._chain = chain
    
    @property
    def id(self) -> int:
        return super().id
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, LinkedListRequest):
            request = cast(LinkedListRequest, other)
            return self.id == request.id
        return False
