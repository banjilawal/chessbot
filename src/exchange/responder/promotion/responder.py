# src/exchange/responder/promotion/responder.py

"""
Module: exchange.responder.promotion.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import PromotionResult
from exchange import PromotionRequest, Responder
from util import LoggingLevelRouter


class PromotionResponder(Responder[PromotionResult]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the promotion Request-Response workflow.

    Attributes:
        
        dispatcher: PromotionDispatcher

    Provides:
        -   def submit(request: PromotionRequest) -> PromotionResponse


    Super Class:
        Responder
    """
    
    def __init__(self, dispatcher: PromotionDispatcher):
        """
        Args:
            dispatcher: PromotionDispatcher
        """
        super().__init__(dispatcher=dispatcher)
        
    @property
    def dispatcher(self) -> PromotionDispatcher:
        return cast(PromotionDispatcher, super().dispatcher)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionRequest) -> PromotionResponse:
        """
        Args:
            request: PromotionRequest
        Result:
            PromotionResponse
        Raises:
            ValidationResponderException
        """
        pass