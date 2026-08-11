# src/request/chain/offset/remove/request.py

"""
Module: request.chain.offset.remove.request
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from authorization import ChainOffsetRequest
from collection import Chain


class RemoveByOffsetRequest(ChainOffsetRequest):
    """
    Role:
        -  Request
        -  Data Transport
    
    Responsibilities:
        1. Carry information for removing a Node from a Chain at an offset.
    
    Attributes:
        id: int
        offset: int
        chain: Chain
        
    Provides:
    
    Super Class:
        ChainItemDeletionRequest
    """
    
    def __init__(self, id: int, chain: Chain, offset: int,):
        """
        Args:
            id: int
            offset: int
            chain: Chain
        """
        super().__init__(id=id, chain=chain, offset=offset)

    