# src/exchange/responder/fabrication/model/responder.py

"""
Module: exchange.responder.fabrication.model.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import ModelBuildResponse
from exchange import ModelBuildRequest, BuildResponder
from transit import ModelBuildDispatcher
from util import LoggingLevelRouter

T = TypeVar("T",)

class ModelBuildResponder(BuildResponder[T], ABC, Generic[T]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Model build Request-Response workflow.

    Attributes:
        dispatcher: ModelBuildDispatcher[T]

    Provides:
        -   def submit(request: ModelBuildRequest[T]) -> ModelBuildResponse[T]

    Super Class:
        ValidatorExchange
    """
    
    def __init__(self, dispatcher: ModelBuildDispatcher[T]):
        """
        Args:
            dispatcher: ModelBuildDispatcher[T]
        """
        super().__init__(dispatcher=dispatcher)
        
    @property
    def dispatcher(self) -> ModelBuildDispatcher[T]:
        return cast(ModelBuildDispatcher, super().dispatcher)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: ModelBuildRequest[T]
    ) -> ModelBuildResponse[T]:
        """
        Args:
            request: ModelBuildRequest[T]
        Result:
            ModelBuildResponse[T]
        Raises:
            ModelValidationResponderException
        """
        pass