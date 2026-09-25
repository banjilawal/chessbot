# src/client/client.py

"""
Module: client.client
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import Response, Result
from client import Request
from transit import Dispatcher
from util import LoggingLevelRouter

T = TypeVar("T", bound="Result")

class Client(ABC, Generic[T]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Request-Response workflow.
        2.  Sends an Originator's Request to a Dispatcher.
        3.  Prepares then forwards a Response to the Originator.

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
    def transmit(self, request: Request[T]) -> Response[T]:
        """
        Args:
            request: Request[T]
        Result:
            Response[T]
        Raises:
            ClientException
        """
        pass