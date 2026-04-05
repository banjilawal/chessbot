# src/logic/system/work/worker.py

"""
Module: logic.system.work.worker
Author: Banji Lawal
Created: 2026-03-30
Version: 1.0.0
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from system import LoggingLevelRouter, TransactionResult

T = TypeVar("T")

class Worker(ABC, Generic[T]):
    """
    Role
        -   Worker
        -   Stateless

    Responsibilities:
        1.  Execute a job on a Data-Holder that produces a TransactionResult.

    Attributes:

    Provides:
        -   work(*args, **kwargs) -> Result[Any]

    super Class:
    """
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def work(self, *args, **kwargs) -> TransactionResult[Any]:
        pass