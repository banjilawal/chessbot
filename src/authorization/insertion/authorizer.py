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
from report import AuthorizationDecision
from domain.exchange.request import InsertionRequest
from toolkit import InsertRequestToolkit

from util import LoggingLevelRouter

T = TypeVar("T", bound="DomainObjectCollection")

class InsertionRequestAuthorizer(RequestAuthorizer[InsertionRequest], ABC, Generic[T]):
    
    def __init__(self, toolkit: InsertRequestToolkit[T]):
        """
        Args:
            toolkit: InsertionRequestToolkit[T]
        """
        super().__init__(toolkit=toolkit)
        
    @property
    def toolkit(self) -> InsertRequestToolkit[T]:
        return cast(InsertRequestToolkit, super().toolkit)
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: InsertionRequest[T]) -> AuthorizationDecision:
        pass