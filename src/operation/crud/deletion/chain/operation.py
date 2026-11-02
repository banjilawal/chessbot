# src/operation/crud/delete/chain/operator.py

"""
Module: operation.crud.delete.chain.operation
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from authorization import RemoveNodeRequest
from repo.collection import Chain
from operation import CollectionDeletion
from artifcat import DeletionResult
from util import LoggingLevelRouter

T = TypeVar("T", bound="Node")


class RemoveNode(CollectionDeletion[Chain], ABC, Generic[T]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Remove a Node from a Chain.

    Attributes:
        dispatcher: RemoveNodeDispatcher[T]

    Provides:
        -   def execute(request: AddNodeRequest) -> DeletionResult

    Super Class:
        DeletionOperation
    """
    
    def __init__(self, dispatcher: RemoveNodeDispatcher[T]):
        """
        Args:
            dispatcher: AddChainNodeDispatcher[T]
        """
        super().__init__(dispatcher=dispatcher)
        
    @property
    def dispatcher(self) -> RemoveNodeDispatcher[T]:
        return cast(RemoveNodeDispatcher[T], super().dispatcher)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: RemoveNodeRequest[T]) -> DeletionResult[T]:
        pass