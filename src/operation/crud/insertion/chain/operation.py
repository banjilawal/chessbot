# src/operation/crud/insertion/chain/operator.py

"""
Module: operation.crud.insertion.chain.operation
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from authorization import AddNodeRequest
from repo.collection import Chain
from operation import InsertionOperation
from artifcat import InsertionionResult
from util import LoggingLevelRouter

T = TypeVar("T", bound="Node")


class AddNode(InsertionOperation[Chain], ABC, Generic[T]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Add a node to a Chain.

    Attributes:
        dispatcher: AddNodeDispatcher

    Provides:
        -   def execute(request: AddNodeRequest) -> InsertionionResult

    Super Class:
        InsertionionOperation
    """
    
    def __init__(self, dispatcher: AddNodeDispatcher):
        """
        Args:
            dispatcher: AddNodeDispatcher
        """
        super().__init__(dispatcher=dispatcher)
        
    @property
    def dispatcher(self) -> AddNodeDispatcher:
        return cast(AddNodeDispatcher, super().dispatcher)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: AddNodeRequest) -> InsertionionResult:
        pass