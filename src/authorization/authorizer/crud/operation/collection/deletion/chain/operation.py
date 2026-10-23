# src/operation/collection/deletion/chain/operation.py

"""
Module: operation.collection.deletion.chain.operation
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
        - Worker

    Responsibilities:
        1.  Remove a Node from a Chain.

    Attributes:
        authorizer: RemoveNodeAuthorizer[T]

    Provides:
        -   def execute(request: AddNodeRequest) -> DeletionResult

    Super Class:
        DeletionOperation
    """
    
    def __init__(self, authorizer: RemoveNodeAuthorizer[T]):
        """
        Args:
            authorizer: AddChainNodeAuthorizer[T]
        """
        super().__init__(authorizer=authorizer)
        
    @property
    def authorizer(self) -> RemoveNodeAuthorizer[T]:
        return cast(RemoveNodeAuthorizer[T], super().authorizer)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: RemoveNodeRequest[T]) -> DeletionResult[T]:
        pass