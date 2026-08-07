# src/authorization/request/chain/request.py

"""
Module: authorization.request.chain.request
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from authorization import Request
from collection import Chain




class ChainRequest(Request):
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
    _chain: Chain
    
    def __init__(self, id: int, chain: Chain, ):
        """
        Args:
            id: int
            chain: Chain
        """
        super().__init__(id=id)
        self._chain = chain
    
    @property
    def id(self) -> int:
        return super().id
    
    @property
    def chain(self) -> chain:
        return self._chain
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ChainRequest):
            return super().__eq__(other)
        return False
