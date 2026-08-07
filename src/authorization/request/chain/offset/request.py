# src/authorization/request/chain/offset/request.py

"""
Module: authorization.request.chain.offset.request
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from authorization import ChainRequest
from collection import Chain


class ChainOffsetRequest(ChainRequest):
    """
    Role:
        -  Request

    Responsibilities:
        1. Carry information for modifying a Chain by an offset.
    
    Attributes:
        offset: int
    
    Provides:
    
    Super Class:
        ChainRequest
    """
    _offset: int
    
    def __init__(self, id: int, chain: Chain, offset: int,):
        """
        Args:
            id: int
            offset: int
            chain: Chain
        """
        super().__init__(id=id, chain=chain)
        self._offset = offset
    
    @property
    def offset(self) -> int:
        return self._offset