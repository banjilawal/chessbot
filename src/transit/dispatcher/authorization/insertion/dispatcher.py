# src/transit/dispatcher/authorization/insertion/dispatcher.py

"""
Module: transit.dispatcher.authorization.insertion.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from authorization import InsertionRequestAuthorizer
from collection import DomainObjectCollection
from transit.dispatcher import AuthorizationDispatcher
from report import AuthorizationDecision
from domain.exchange.request import InsertionRequest
from result import InsertionResult
from util import LoggingLevelRouter

T = TypeVar("T", bound="DomainObjectCollection")

class InsertionDispatcher(AuthorizationDispatcher[InsertionResult], ABC, Generic[T]):
    
    def __init__(self, authorizer: InsertionRequestAuthorizer[T]):
        """
        Args:
            authorizer: InsertionRequestAuthorizer[T]
        """
        super().__init__(authorizer=authorizer)
    
    @property
    def authorizer(self) -> InsertionRequestAuthorizer[T]:
        return cast(InsertionRequestAuthorizer[T], super().authorizer)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: InsertionRequest[T]) -> AuthorizationDecision:
        pass