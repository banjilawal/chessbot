# src/transit/dispatcher/response/dispatcher.py

"""
Module: transit.dispatcher.response.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from exchange import Request
from util import LoggingLevelRouter

T = TypeVar("T", bound="Result")

class ResponseDispatcher(ABC, Generic[T]):
    """
    Role
        -   Messaging 

    Responsibilities:
        1.  Interface for Responder

    Attributes:
        responsder: Responsder[T]

    Provides:
        -   def execute(self, request[T]) -> Any

    Super Class:
        Dispatcher
    """
    _responder: Responder
    
    def __init__(self, responder: Responsder[T]):
        """
        Args:
            responder: Responsder[T]
        """
        self._responder = responder
        
    @property
    def responsder(self) ->Responsder[T]:
        return self._responsder
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: Request[T]) -> Any:
        pass