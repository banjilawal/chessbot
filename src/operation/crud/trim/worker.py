# src/operation/crud/trim/operator.py

"""
Module: operation.crud.trim.operation
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from authorization import TrimPermitter
from operation import CrudWorker, NodeSearcher
from artifcat import TrimResult
from request import TrimRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="TrimRequest")


class ChainTrimmer(CrudWorker[TrimResult], ABC, Generic[T]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Process an TrimRequest.

    Attributes:
        permitter: TrimPermitter

    Provides:
        -   def execute(request: Q) -> TrimResult

    Super Class:
        CrudOperation
    """
    _searcher: NodeSearcher
    
    def __init__(self, searcher: NodeSearcher, permitter: TrimChainPermitter,):
        """
        Args:
            searcher: NodeSearcher
            permitter: TrimChainPermitter
        """
        super().__init__(permitter=permitter)
        self._searcher = searcher
    
    @property
    def searcher(self) -> NodeSearcher:
        return self._searcher
    
    @property
    def permitter(self) -> TrimChainPermitter:
        return cast(TrimPermitter, super().permitter)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: Q) -> TrimResult:
        """
        Args:
            request: Q
        Result:
            TrimResult
        Raises:
            TrimException
        """
        pass