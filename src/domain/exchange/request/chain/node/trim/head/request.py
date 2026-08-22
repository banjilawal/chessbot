# src/domain/exchange/request/chain/node/trim/head/request.py

"""
Module: domain.exchange.request.chain.node.trim.head.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar

from authorization import ChainOffsetRequest, ChainTrimByNodeRequest
from collection import Chain

T = TypeVar("T", bound="Node")


class TrimHeadNodeRequest(ChainTrimByNodeRequest, ABC, Generic[T]):
    """
    Role:
        -  Request
    
    Responsibilities:
        1. Carry information for trimming a Chain from its head to a target node.

    Attributes:
        id: int
        node: T
        chain: Chain[T]
        offset_request: Optional[ChainOffsetRequest]

    Provides:

    Super Class:
        ChainTrimByNodeRequest
    """
    
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
        super().__init__(id=id, node=node, chain=chain, offset_request=offset_request)

    