# src/authorization/adjudicator/chain/node/append/request.py

"""
Module: authorization.adjudicator.chain.node.append.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar

from authorization import ChainNodeRequest, ChainOffsetRequest
from collection import Chain


T = TypeVar("T", bound="Node")


class AppendNodeRequest(ChainNodeRequest, ABC, Generic[T]):
    """
    Role:
        -  Request

    Responsibilities:
        1. Carry Node information for appending a Node to a Chain.

    Attributes:
        id: int
        node: T
        chain: Chain[T]
        offset_request: Optional[ChainOffsetRequest]

    Provides:

    Super Class:
        ChainNodeRequest
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

    