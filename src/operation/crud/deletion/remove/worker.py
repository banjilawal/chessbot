# src/operation/crud/deletion/remove/operator.py

"""
Module: operation.crud.deletion.remove.operation
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import DeletionResult
from authorization import RemoveNodePermitter
from operation import Deleter, NodeSearcher
from request import RemoveNodeRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="RemoveNodeRequest")


class NodeRemover(Deleter[T], ABC, Generic[T]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Remove a Node from a Chain.

    Attributes:
        searcher: NodeSearcher
        permitter: RemoveNodePermitter

    Provides:
        -   def execute(request: AddNodeRequest) -> DeletionResult

    Super Class:
        Deleter
    """
    _searcher: NodeSearcher
    
    def __init__(self, searcher: NodeSearcher, permitter: RemoveNodePermitter,):
        """
        Args:
            searcher: NodeSearcher
            permitter: AddChainNodePermitter
        """
        super().__init__(permitter=permitter)
        self._searcher = searcher
    
    @property
    def searcher(self) -> NodeSearcher:
        return self._searcher
        
    @property
    def permitter(self) -> RemoveNodePermitter:
        return cast(RemoveNodePermitter, super().permitter)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> DeletionResult:
        pass