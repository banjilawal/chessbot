# src/operation/collection/insertion/chain/vector/operation.py

"""
Module: operation.collection.insertion.chain.vector.operation
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from authorization import AddVectorNodeRequest
from domain.struct.node import VectorNode
from operation import AddNode
from artifcat import InsertionResult
from util import LoggingLevelRouter


class AddVectorNode(AddNode[VectorNode]):
    """
    Role
        - Worker

    Responsibilities:
        1.  Add an item to a VectorNodeChain.
        
    Attributes:
        authorizer: AddVectorNodeAuthorizer

    Provides:
        -   def execute(request: AddVectorNodeRequest) -> InsertionResult

    Super Class:
        AddChainNode
    """
    
    def __init__(self, authorizer: Optional[AddVectorNodeAuthorizer] | None = None):
        """
        Args:
            authorizer: Optional[AddVectorNodeAuthorizer]
        """
        super().__init__(authorizer=authorizer or AddVectorNodeAuthorizer())
    
    @property
    def authorizer(self) -> AddVectorNodeAuthorizer:
        return cast(AddVectorNodeAuthorizer, super().authorizer)
    

    @LoggingLevelRouter.monitor
    def execute(self, request: AddVectorNodeRequest) -> InsertionResult:
        pass