# src/exchange/responder/fabrication/responder.py

"""
Module: exchange.responder.fabrication.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import BuildResponse, BuildResult
from exchange import Responder, BuildRequest
from transit import BuildDispatcher
from util import LoggingLevelRouter

T = TypeVar("T",)

class BuildResponder(Responder[BuildResult], ABC, Generic[T]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the build Request-Response workflow.

    Attributes:
        dispatcher: BuildDispatcher[T]

    Provides:
        -   def submit(request: BuildRequest[T]) -> BuildResponse[T]

    Super Class:
        Exchange
    """
    
    def __init__(self, dispatcher: BuildDispatcher[T]):
        """
        Args:
            dispatcher: BuildDispatcher[T]
        """
        super().__init__(dispatcher=dispatcher)
        
    @property
    def dispatcher(self) -> BuildDispatcher[T]:
        return cast(BuildDispatcher, super().dispatcher)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: BuildRequest[T]) -> BuildResponse[T]:
        """
        Args:
            request: BuildRequest[T]
        Result:
            BuildResponse[T]
        Raises:
            ValidatorExchangeException
        """
        pass