# src/exchange/responder/validation/struct/node/exchange.py

"""
Module: exchange.responder.validation.struct.node.exchange
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import NodeValidationResponse
from exchange import NodeValidationRequest, ValidationResponder
from transit import NodeValidationDispatcher
from util import LoggingLevelRouter

T = TypeVar("T",)

class NodeValidationResponder(
    ValidationResponder[T],
    ABC,
    Generic[T],
):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Node validation Request-Response workflow.

    Attributes:
        dispatcher: NodeValidationDispatcher[T]

    Provides:
        -   def submit(request: NodeValidationRequest[T]) -> NodeValidationResponse[T]

    Super Class:
        ValidatorExchange
    """
    
    def __init__(self, dispatcher: NodeValidationDispatcher[T]):
        """
        Args:
            dispatcher: NodeValidationDispatcher[T]
        """
        super().__init__(dispatcher=dispatcher)
        
    @property
    def dispatcher(self) -> NodeValidationDispatcher[T]:
        return cast(NodeValidationDispatcher, super().dispatcher)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: NodeValidationRequest[T]
    ) -> NodeValidationResponse[T]:
        """
        Args:
            request: NodeValidationRequest[T]
        Result:
            NodeValidationResponse[T]
        Raises:
            NodeValidatorExchangeException
        """
        pass