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
from operation import CrudWorker
from artifcat import TrimResult
from request import TrimRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="TrimRequest")


class Trimmer(CrudWorker[TrimResult], ABC, Generic[T]):
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
    
    def __init__(self, permitter: TrimPermitter):
        """
        Args:
            permitter: TrimPermitter
        """
        super().__init__(permitter=permitter)
    
    @property
    def permitter(self) -> TrimPermitter:
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