# src/client/operator.py

"""
Module: client.client
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import Result
from domain import Request
from transit import Dispatcher
from util import LoggingLevelRouter

T = TypeVar("T", bound="Result")

class Client(ABC, Generic[T]):
    """
    Role
        - Client

    Responsibilities:
        1.  Submit a request to a Dispatcher

    Attributes:
        dispatcher: Dispatcher[T]
        
    Provides:
        -   def submit(request: Request[T]) -> T

    Super Class:
    """
    _dispatcher: Dispatcher[T]
    
    def __init__(self, dispatcher: Dispatcher[T]):
        """
        Args:
            dispatcher: Dispatcher[T]
        """
        self._dispatcher = dispatcher
        
    @property
    def dispatcher(self) -> Dispatcher[T]:
        return self._dispatcher
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def submit(self, request: Request[T]) -> T:
        """
        Args:
            request: Request[T]
        Result:
            T
        Raises:
            ClientException
        """
        pass