# src/request/chain/offset/trim/request.py

"""
Module: request.chain.offset.trim.request
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from authorization import ChainOffsetRequest
from collection import Chain


class TrimByOffsetRequest(ChainOffsetRequest):
    """
    Role:
        -  Request
    
    Responsibilities:
        1. Carry information for modifying a Chain by an offset.
    
    Attributes:
        id: int
        offset: int
        chain: Chain
        
    Provides:
    
    Super Class:
        ChainRequest
    """
    
    def __init__(self, id: int, chain: Chain, offset: int,):
        """
        Args:
            id: int
            offset: int
            chain: Chain
        """
        super().__init__(id=id, chain=chain, offset=offset)

    