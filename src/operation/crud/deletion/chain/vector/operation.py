# src/operation/crud/delete/chain/vector/operator.py

"""
Module: operation.crud.delete.chain.vector.operation
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from authorization import RemoveVectorNodeRequest
from domain.struct.node import VectorNode
from operation import RemoveNode
from artifcat import DeletionResult
from util import LoggingLevelRouter


class RemoveVectorNode(RemoveNode[VectorNode]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Add an item to a VectorNodeChain.
        
    Attributes:
        dispatcher: RemoveVectorNodeDispatcher

    Provides:
        -   def execute(request: RemoveVectorNodeRequest) -> DeletionResult

    Super Class:
        RemoveNode
    """
    
    def __init__(self, dispatcher: Optional[RemoveVectorNodeDispatcher] | None = None):
        """
        Args:
            dispatcher: Optional[RemoveVectorNodeDispatcher]
        """
        super().__init__(dispatcher=dispatcher or RemoveVectorNodeDispatcher())
    
    @property
    def dispatcher(self) -> RemoveVectorNodeDispatcher:
        return cast(RemoveVectorNodeDispatcher, super().dispatcher)
    

    @LoggingLevelRouter.monitor
    def execute(self, request: RemoveVectorNodeRequest) -> DeletionResult[VectorNode]:
        pass