# src/transport/queue/queue.py

"""
Module: transport.queue.queue
Author: Banji Lawal
Created: 2026-03-30
version: 1.0.0
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Iterator, List, TypeVar

from logic.system import DeletionResult, InsertionResult, LoggingLevelRouter
from transport import Message

M = TypeVar("M", bound=Message)

class MessageQueue(ABC, Generic[M]):
    
    @property
    @abstractmethod
    def messages(self) -> List[M]:
        pass
    
    @property
    @abstractmethod
    def iterator(self) -> Iterator[M]:
        pass
    
    @property
    @abstractmethod
    def size(self) -> int:
        pass
    
    @property
    @abstractmethod
    def is_empty(self) -> bool:
        pass
    
    @LoggingLevelRouter.monitor
    def enqueue(self, message: M) -> InsertionResult:
        pass
    
    @LoggingLevelRouter.monitor
    def dequeue(self) -> DeletionResult[M]:
        pass
    