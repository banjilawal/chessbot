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
from collection import Chain
from operation import CollectionDeletion
from artifcat import DeletionResult
from util import LoggingLevelRouter

T = TypeVar("T", bound="Node")


class RemoveNode(CollectionDeletion[Chain], ABC, Generic[T]):
    """
    Role
        -  Worker

    Responsibilities:
        1.  Remove a Node from a Chain.

    Attributes:
        permitter: RemoveNodePermitter[T]

    Provides:
        -  def execute(request: AddNodeRequest) -> DeletionResult

    Super Class:
        DeletionOperation
    """
    
    def __init__(self, permitter: RemoveNodePermitter[T]):
        """
        Args:
            permitter: AddChainNodePermitter[T]
        """
        super().__init__(permitter=permitter)
        
    @property
    def permitter(self) -> RemoveNodePermitter[T]:
        return cast(RemoveNodePermitter[T], super().permitter)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: RemoveNodeRequest[T]) -> DeletionResult[T]:
        pass