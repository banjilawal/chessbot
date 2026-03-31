# src/transport/queue/queue.py

"""
Module: transport.queue.queue
Author: Banji Lawal
Created: 2026-03-30
version: 1.0.0
"""

from __future__ import annotations

from typing import Iterator, List, Optional

from logic.system import InsertionResult, LoggingLevelRouter
from transport import MessageQueue, ServiceRequest

class ServiceRequestQueue(MessageQueue[ServiceRequest]):
   
    _messages: List[ServiceRequest]
    
    def __init__(self,):
        self._messages = []
    
    @property
    def messages(self) -> List[ServiceRequest]:
        return self._messages
    
    @property
    def iterator(self) -> Iterator[ServiceRequest]:
        return iter(self._messages)
    
    @property
    def size(self) -> int:
        return len(self._messages)
    
    @property
    def is_empty(self) -> bool:
        return len(self._messages) == 0
    
    @LoggingLevelRouter.monitor
    def enqueue(self, message: ServiceRequest) -> InsertionResult:
        pass
    
    @LoggingLevelRouter.monitor
    def dequeue(self) -> Optional[ServiceRequest]:
        pass
    