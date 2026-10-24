# src/transit/dispatcher/promotion/dispatcher.py

"""
Module: transit.dispatcher.promotion.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod

from artifcat import PromotionResponse
from exchange import PromotionRequest
from transit import Dispatcher
from util import LoggingLevelRouter

class PromotionDispatcher(Dispatcher[PromotionRequest]):
    """
    Role
        -   Permission Promotion Manager

    Responsibilities:
        1.  Grant

    Attributes:
        promoter: Promoter

    Provides:
        -   def  execute(self, request: PromotionRequest) -> PromotionResponse

    Super Class:
        Dispatcher
    """
    
    _promoter: Promoter
    
    def __init__(self, promoter: Promoter):
        """
        Args:
            promoter: Promoter
        """
        self._promoter = promoter
        
    @property
    def promoter(self) -> Promoter:
        return self._promoter
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionRequest) -> PromotionResponse:
        """
        Decide if an activity can be performed.
        Args:
            request: T
        Returns:
            PromotionResponse
        Raises:
            PromotionDispatcherException
        """
        pass