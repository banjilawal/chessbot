# src/exchange/responder/fabrication/struct/node/responder.py

"""
Module: exchange.responder.fabrication.struct.node.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import NodeBuildResponse
from exchange import NodeBuildRequest, BuildResponder
from transit import NodeBuildDispatcher
from util import LoggingLevelRouter

T = TypeVar("T",)

class NodeBuildResponder(
    BuildResponder[T],
    ABC,
    Generic[T],
):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Node build Request-Response workflow.

    Attributes:
        dispatcher: NodeBuildDispatcher[T]

    Provides:
        -   def execute(request: NodeBuildRequest[T]) -> NodeBuildResponse[T]

    Super Class:
        ValidatorExchange
    """
    
    def __init__(self, dispatcher: NodeBuildDispatcher[T]):
        """
        Args:
            dispatcher: NodeBuildDispatcher[T]
        """
        super().__init__(dispatcher=dispatcher)
        
    @property
    def dispatcher(self) -> NodeBuildDispatcher[T]:
        return cast(NodeBuildDispatcher, super().dispatcher)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: NodeBuildRequest[T]
    ) -> NodeBuildResponse[T]:
        """
        Args:
            request: NodeBuildRequest[T]
        Result:
            NodeBuildResponse[T]
        Raises:
            NodeValidationResponderException
        """
        pass