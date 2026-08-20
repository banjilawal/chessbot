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
from collection import Collection
from report import AuthorizationDecision
from request import InsertionRequest
from toolkit import InsertionRequestToolkit

from util import LoggingLevelRouter

T = TypeVar("T", bound="Collection")

class InsertionRequestAuthorizer(RequestAuthorizer[InsertionRequest], ABC, Generic[T]):
    
    def __init__(self, toolkit: InsertionRequestToolkit[T]):
        """
        Args:
            toolkit: InsertionRequestToolkit[T]
        """
        super().__init__(toolkit=toolkit)
        
    @property
    def toolkit(self) -> InsertionRequestToolkit[T]:
        return cast(InsertionRequestToolkit, super().toolkit)
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: InsertionRequest[T]) -> AuthorizationDecision:
        pass