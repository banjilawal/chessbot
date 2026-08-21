# src/authorization/adjudicator/chain/node/remove/request.py

"""
Module: authorization.adjudicator.chain.node.remove.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from authorization import RemoveNodeRequest, ChainOffsetRequest
from collection import VectorChain
from domain.node import VectorNode


class RemoveVectorNodeRequest(RemoveNodeRequest[VectorNode]):
    """
    Role:
        -  Request

    Responsibilities:
        1. Carry information about which node to remove from a VectorChain.

    Attributes:
        id: int
        node: VectorNode
        chain: VectorChain
        offset_request: Optional[ChainOffsetRequest]

    Provides:

    Super Class:
        RemoveNodeRequest
    """

    def __init__(self,
            id: int,
            node: VectorNode,
            chain: VectorChain,
            offset_request: Optional[ChainOffsetRequest] | None = None,
    ):
        """
        Args:
            id: int
            node: VectorNode,
            chain: VectorChain,
            offset_request: Optional[ChainOffsetRequest]
        """
        super().__init__(id=id, node=node, chain=chain, offset_request=offset_request)
        
    @property
    def node(self) -> VectorNode:
        return cast(VectorNode, super().node)
    
    @property
    def chain(self) -> VectorChain:
        return cast(VectorChain, super().chain)

    