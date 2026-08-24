# src/authorization/insertion/authorization.py

"""
Module: authorization.insertion.authorization
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from authorization import RequestAuthorizer
from collection import DomainObjectCollection
from artifcat.report import AuthorizationDecision
from domain.exchange.request import InsertionRequest
from operation.utility import InsertPermissionUtility

from util import LoggingLevelRouter

T = TypeVar("T", bound="DomainObjectCollection")

class InsertionRequestAuthorizer(RequestAuthorizer[InsertionRequest], ABC, Generic[T]):
    
    def __init__(self, utility: InsertPermissionUtility[T]):
        """
        Args:
            utility: InsertionPermissionUtility[T]
        """
        super().__init__(utility=utility)
        
    @property
    def utility(self) -> InsertPermissionUtility[T]:
        return cast(InsertPermissionUtility, super().utility)
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: InsertionRequest[T]) -> AuthorizationDecision:
        pass