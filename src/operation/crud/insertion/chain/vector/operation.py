# src/operation/crud/insertion/chain/vector/operator.py

"""
Module: operation.crud.insertion.chain.vector.operation
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from authorization import AddVectorNodeRequest
from domain.struct.node import VectorNode
from operation import AddNode
from artifcat import InsertionionResult
from util import LoggingLevelRouter


class AddVectorNode(AddNode[VectorNode]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Add an item to a VectorNodeChain.
        
    Attributes:
        dispatcher: AddVectorNodeDispatcher

    Provides:
        -   def execute(request: AddVectorNodeRequest) -> InsertionionResult

    Super Class:
        AddChainNode
    """
    
    def __init__(self, dispatcher: Optional[AddVectorNodeDispatcher] | None = None):
        """
        Args:
            dispatcher: Optional[AddVectorNodeDispatcher]
        """
        super().__init__(dispatcher=dispatcher or AddVectorNodeDispatcher())
    
    @property
    def dispatcher(self) -> AddVectorNodeDispatcher:
        return cast(AddVectorNodeDispatcher, super().dispatcher)
    

    @LoggingLevelRouter.monitor
    def execute(self, request: AddVectorNodeRequest) -> InsertionionResult:
        pass