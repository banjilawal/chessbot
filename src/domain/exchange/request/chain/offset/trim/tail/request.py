# src/domain/exchange/request/chain/offset/trim/tail/request.py

"""
Module: domain.exchange.request.chain.offset.trim.tail.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from authorization import ChainOffsetRequest
from collection import Chain


class TrimTailByOffsetRequest(ChainOffsetRequest):
    """
    Role:
        - Request
        -  Data Transport
    
    Responsibilities:
        1. Carry information for running a ChainTrimByTail operation.
    
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

    