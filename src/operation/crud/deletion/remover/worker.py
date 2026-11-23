# src/operation/crud/deletion/chain/operator.py

"""
Module: operation.crud.deletion.chain.operation
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import DeletionResult
from domain import Node
from operation import Deleter
from util import LoggingLevelRouter

T = TypeVar("T", bound="Node")


class NodeRemover(Deleter, ABC, Generic[T]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Remove a Node from a Chain.

    Attributes:
        permitter: RemoveNodePermitter

    Provides:
        -   def execute(request: AddNodeRequest) -> DeletionResult

    Super Class:
        DeletionOperation
    """
    
    def __init__(self, permitter: RemoveNodePermitter):
        """
        Args:
            permitter: AddChainNodePermitter
        """
        super().__init__(permitter=permitter)
        
    @property
    def permitter(self) -> RemoveNodePermitter:
        return cast(RemoveNodePermitter, super().permitter)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> DeletionResult:
        pass