# src/operation/crud/insert/chain/vector/operator.py

"""
Module: operation.crud.insert.chain.vector.operation
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from authorization import AddVectorNodeRequest
from domain.structure.node import VectorNode
from operation import AddNode
from artifcat import InsertionResult
from util import LoggingLevelRouter


class AddVectorNode(AddNode[VectorNode]):
    """
    Role
        -  Worker

    Responsibilities:
        1.  Add an item to a VectorNodeChain.
        
    Attributes:
        permitter: AddVectorNodePermitter

    Provides:
        - def execute(request: AddVectorNodeRequest) -> InsertionResult

    Super Class:
        AddChainNode
    """
    
    def __init__(self, permitter: Optional[AddVectorNodePermitter] | None = None):
        """
        Args:
            permitter: Optional[AddVectorNodePermitter]
        """
        super().__init__(permitter=permitter or AddVectorNodePermitter())
    
    @property
    def permitter(self) -> AddVectorNodePermitter:
        return cast(AddVectorNodePermitter, super().permitter)
    

    @LoggingLevelRouter.monitor
    def execute(self, request: AddVectorNodeRequest) -> InsertionResult:
        pass