# src/exchange/responder/authorization/struct/node/responder.py

"""
Module: exchange.responder.authorization.struct.node.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import NodeDecision
from exchange import NodeAuthorizationRequest, AuthorizationResponder
from transit import NodeAuthorizationDispatcher
from util import LoggingLevelRouter

T = TypeVar("T",)

class NodeAuthorizationResponder(
    AuthorizationResponder[T],
    ABC,
    Generic[T],
):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Node authorization Request-Response workflow.

    Attributes:
        dispatcher: NodeAuthorizationDispatcher[T]

    Provides:
        -   def execute(request: NodeAuthorizationRequest[T]) -> NodeDecision[T]

    Super Class:
        ValidatorExchange
    """
    
    def __init__(self, dispatcher: NodeAuthorizationDispatcher[T]):
        """
        Args:
            dispatcher: NodeAuthorizationDispatcher[T]
        """
        super().__init__(dispatcher=dispatcher)
        
    @property
    def dispatcher(self) -> NodeAuthorizationDispatcher[T]:
        return cast(NodeAuthorizationDispatcher, super().dispatcher)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: NodeAuthorizationRequest[T]
    ) -> NodeDecision[T]:
        """
        Args:
            request: NodeAuthorizationRequest[T]
        Result:
            NodeDecision[T]
        Raises:
            NodeAuthorizationResponderException
        """
        pass