# src/exchange/responder/fabrication/struct/register/responder.py

"""
Module: exchange.responder.fabrication.struct.register.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import RegisterBuildResponse
from exchange import RegisterBuildRequest, StructBuildResponder
from transit import RegisterBuildDispatcher
from util import LoggingLevelRouter

T = TypeVar("T",)

class RegisterBuildResponder(
    StructBuildResponder[T],
    ABC,
    Generic[T],
):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Register build Request-Response workflow.

    Attributes:
        dispatcher: RegisterBuildDispatcher[T]

    Provides:
        -   def submit(request: RegisterBuildRequest[T]) -> RegisterBuildResponse[T]

    Super Class:
        ValidatorExchange
    """
    
    def __init__(self, dispatcher: RegisterBuildDispatcher[T]):
        """
        Args:
            dispatcher: RegisterBuildDispatcher[T]
        """
        super().__init__(dispatcher=dispatcher)
        
    @property
    def dispatcher(self) -> RegisterBuildDispatcher[T]:
        return cast(RegisterBuildDispatcher, super().dispatcher)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: RegisterBuildRequest[T]
    ) -> RegisterBuildResponse[T]:
        """
        Args:
            request: RegisterBuildRequest[T]
        Result:
            RegisterBuildResponse[T]
        Raises:
            RegisterValidationResponderException
        """
        pass