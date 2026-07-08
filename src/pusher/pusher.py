# src/pusher/pusher.py

"""
Module: pusher.pusher
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from request import PushRequest
from result import InsertionResult
from util import LoggingLevelRouter

T = TypeVar("T")

class Pusher(ABC, Generic[T]):
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: PushRequest) -> InsertionResult:
        pass