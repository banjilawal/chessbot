# src/exchange/responder/promotion/responder.py

"""
Module: exchange.responder.promotion.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from artifcat import PromotionResponse, PromotionResult
from exchange import Responder, PromotionRequest
from transit import PromotionDispatcher
from util import LoggingLevelRouter


class PromotionResponder(Responder[PromotionResult]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the promotion Request-Response workflow.

    Attributes:
        
        dispatcher: PromotionDispatcher[T]

    Provides:
        -   def submit(request: PromotionRequest[T]) -> PromotionResponse[T]


    Super Class:
        Responder
    """
    
    def __init__(self, dispatcher: PromotionDispatcher[T]):
        """
        Args:
            dispatcher: PromotionDispatcher[T]
        """
        super().__init__(dispatcher=dispatcher)
        
    @property
    def dispatcher(self) -> PromotionDispatcher[T]:
        return cast(PromotionDispatcher, super().dispatcher)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionRequest[T]) -> PromotionResponse[T]:
        """
        Args:
            request: PromotionRequest[T]
        Result:
            PromotionResponse[T]
        Raises:
            ValidationResponderException
        """
        pass