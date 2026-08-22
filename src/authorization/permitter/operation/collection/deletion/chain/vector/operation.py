# src/operation/collection/deletion/chain/vector/operation.py

"""
Module: operation.collection.deletion.chain.vector.operation
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from authorization import RemoveVectorNodeRequest
from domain.structure.node import VectorNode
from operation import RemoveNode
from result import DeletionResult
from util import LoggingLevelRouter


class RemoveVectorNode(RemoveNode[VectorNode]):
    """
    Role
        -   Worker

    Responsibilities:
        1.  Add an item to a VectorNodeChain.
        
    Attributes:
        permitter: RemoveVectorNodePermitter

    Provides:
        -   def execute(request: RemoveVectorNodeRequest) -> DeletionResult

    Super Class:
        RemoveNode
    """
    
    def __init__(self, permitter: Optional[RemoveVectorNodePermitter] | None = None):
        """
        Args:
            permitter: Optional[RemoveVectorNodePermitter]
        """
        super().__init__(permitter=permitter or RemoveVectorNodePermitter())
    
    @property
    def permitter(self) -> RemoveVectorNodePermitter:
        return cast(RemoveVectorNodePermitter, super().permitter)
    

    @LoggingLevelRouter.monitor
    def execute(self, request: RemoveVectorNodeRequest) -> DeletionResult[VectorNode]:
        pass