# src/exchange/responder/attack/responder.py

"""
Module: exchange.responder.attack.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import AttackResult
from exchange import Responder
from util import LoggingLevelRouter

T = TypeVar("T", bound="AttackResult")

class AttackResponder(Responder[T], ABC, Generic[T]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the attack Request-Response workflow.

    Attributes:
        dispatcher: AttackDispatcher[T]

    Provides:
        -   def execute(request: AttackRequest[T]) -> AttackResponse[T]


    Super Class:
        Responder
    """
    
    def __init__(self, dispatcher: AttackDispatcher[T]):
        """
        Args:
            dispatcher: AttackDispatcher[T]
        """
        super().__init__(dispatcher=dispatcher)
        
    @property
    def dispatcher(self) -> AttackDispatcher[T]:
        return cast(AttackDispatcher, super().dispatcher)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> AttackResponse[T]:
        """
        Args:
            request: T
        Result:
            AttackResponse[T]
        Raises:
            AttackResponderException
        """
        pass