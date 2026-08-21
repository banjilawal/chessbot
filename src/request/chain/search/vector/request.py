# src/request/chain/search/request.py

"""
Module: request.chain.search.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from authorization import ChainSearchRequest
from collection import VectorChain
from domain.node import VectorNode


class VectorNodeSearchRequest(ChainSearchRequest[VectorNode]):
    """
    Role:
        -  Request

    Responsibilities:
        1. Carry information to find a VectorNode in the a VectorChain.

    Attributes:
        id: int
        target: VectorNode
        chain: VectorChain

    Provides:

    Super Class:
        ChainSearchRequest
    """
    
    def __init__(self, id: int, target: VectorNode, chain: VectorChain,):
        """
        Args:
            id: int
            target: VectorNode
            chain: VectorChain
        """
        super().__init__(id=id, target=target, chain=chain,)
        
    @property
    def target(self) -> VectorNode:
        return cast(VectorNode, super().target)
    
    @property
    def chain(self) -> VectorChain:
        return cast(VectorChain, super().chain)
        