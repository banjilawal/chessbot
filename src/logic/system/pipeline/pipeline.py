# src/logic/system/route/router.py

"""
Module: logic.system.route.router
Author: Banji Lawal
Created: 2026-03-30
Version: 1.0.0
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, TypeVar

from logic.system import InsertionResult, LoggingLevelRouter, Result, StackService
from logic.system.worker import Worker

T = TypeVar("T")

class PipeLine(ABC, Generic[T]):
    """
    Role
        -   Production Line

    Responsibilities:
        1.  Provide the worker with all resources it needs to complete a job.

    Attributes:
            id: int
            name: str
            worker: Worker[T]
            queue: StackService[T]

    Provides:
        -   enqueue(job: T) -> InsertionResult
        -   dequeue() -> Result[Any]

    super Class:
    """
    _id: int
    _name: str
    _worker: Worker[T]
    _queue: StackService[T]
    
    def __init__(
            self,
            id: int,
            name: str,
            worker: Worker[T],
            queue: StackService[T]
    ):
        """
        Args:
            id: int
            name: str
            worker: Worker[T]
            queue: StackService[T]
        """
        self.id = id
        self.name = name
        self._queue = queue
        self._worker = worker

    @property
    def id(self) -> int:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    @abstractmethod
    def is_empty(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def number_of_jobs(self) -> int:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def enqueue(self, job: T) -> InsertionResult:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def dequeue(self) -> Result[Any]:
        pass