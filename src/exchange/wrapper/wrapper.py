# src/exchange/wrapper/wrapper.py

"""
Module: exchange.wrapper.wrapper
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from artifcat import Result
from exchange import Request, Responder
from util import LoggingLevelRouter

T = TypeVar("T", bound="Result")

class ResponseWrapper(ABC, Generic[T]):
    """
    Role
        -   Wrapper

    Responsibilities:
        1.  Extract the payload from a Response.result attribute

    Attributes:
        responder: Responder[T]

    Provides:
        -   def execute(self, request[T]) -> Any

    Super Class:
    """
    _responder: Responder[T]
    
    def __init__(self, responder: Responder[T]):
        """
        Args:
            responder: Responder[T]
        """
        self._responder = responder
        
    @property
    def responder(self) ->Responder[T]:
        return self._responder
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: Request[T]) -> Any:
        pass