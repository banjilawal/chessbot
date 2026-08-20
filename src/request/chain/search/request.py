# src/request/chain/search/request.py

"""
Module: request.chain.search.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from authorization import ChainRequest
from collection import Chain


T = TypeVar("T", bound="Node")


class ChainSearchRequest(ChainRequest, ABC, Generic[T]):
    """
    Role:
        -  Request

    Responsibilities:
        1. Carry information for firing a Node search in a Chain.

    Attributes:
        id: int
        target: T
        chain: Chain[T]

    Provides:

    Super Class:
        ChainRequest
    """
    _target: T
    
    def __init__(self, id: int, target: T, chain: Chain[T],):
        """
        Args:
            id: int
            target: T
            chain: Chain[T]
        """
        super().__init__(id=id, chain=chain,)
        self._target = target
        
    @property
    def target(self) -> T:
        return self._target
        