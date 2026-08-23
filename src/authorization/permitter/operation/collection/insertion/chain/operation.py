# src/operation/collection/insertion/chain/operation.py

"""
Module: operation.collection.insertion.chain.operation
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from authorization import AddNodeRequest
from collection import Chain
from operation import InsertOperation
from artifcat.result import InsertionResult
from util import LoggingLevelRouter

T = TypeVar("T", bound="Node")


class AddNode(InsertOperation[Chain], ABC, Generic[T]):
    """
    Role
        -   Worker

    Responsibilities:
        1.  Add a node to a Chain.

    Attributes:
        permitter: AddNodePermitter[T]

    Provides:
        -   def execute(request: AddNodeRequest) -> InsertionResult

    Super Class:
        InsertionOperation
    """
    
    def __init__(self, permitter: AddNodePermitter[T]):
        """
        Args:
            permitter: AddNodePermitter[T]
        """
        super().__init__(permitter=permitter)
        
    @property
    def permitter(self) -> AddNodePermitter[T]:
        return cast(AddNodePermitter[T], super().permitter)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: AddNodeRequest) -> InsertionResult:
        pass