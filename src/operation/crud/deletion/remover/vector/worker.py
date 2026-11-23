# src/operation/crud/deletion/chain/vector/operator.py

"""
Module: operation.crud.deletion.chain.vector.operation
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import VectorNode
from operation import VectorNodeRemover
from artifcat import DeletionResult
from request import RemoveVectorNodeRequest
from util import LoggingLevelRouter


class VectorNodeRemover(VectorNodeRemover[RemoveVectorNodeRequest]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Add an item to a VectorNodeChain.
        
    Attributes:
        permitter: RemoveVectorNodePermitter

    Provides:
        -   def execute(request: RemoveVectorNodeRequest) -> DeletionResult

    Super Class:
        VectorNodeRemover
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