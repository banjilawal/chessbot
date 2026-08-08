# src/authorization/request/chain/node/request.py

"""
Module: authorization.request.chain.node.request
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar

from authorization import ChainOffsetRequest, ChainRequest
from collection import Chain


T = TypeVar("T", bound="Node")


class ChainNodeRequest(ChainRequest, ABC, Generic[T]):
    """
    Role:
        -  Request

    Responsibilities:
        1. Carry Node information for a Chain's CRUD operation.

    Attributes:
        id: int
        node: T
        chain: Chain[T]
        offset_request: Optional[ChainOffsetRequest]

    Provides:

    Super Class:
        ChainNodeRequest
    """
    _node: T
    
    def __init__(
            self,
            id: int,
            node: T,
            chain: Chain[T],
            offset_request: Optional[ChainOffsetRequest] | None = None,
    ):
        """
        Args:
            id: int
            node: T
            chain: Chain[T]
            offset_request: Optional[ChainOffsetRequest]
        """
        super().__init__(id=id, chain=chain, offset_request=offset_request)
        self._node = node
        
    @property
    def node(self) -> T:
        return self._node