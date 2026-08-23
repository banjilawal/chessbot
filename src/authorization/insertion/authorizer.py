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
from operation.toolkit import InsertPermissionRuleset

from util import LoggingLevelRouter

T = TypeVar("T", bound="DomainObjectCollection")

class InsertionRequestAuthorizer(RequestAuthorizer[InsertionRequest], ABC, Generic[T]):
    
    def __init__(self, ruleset: InsertPermissionRuleset[T]):
        """
        Args:
            ruleset: InsertionRequestToolkit[T]
        """
        super().__init__(ruleset=ruleset)
        
    @property
    def ruleset(self) -> InsertPermissionRuleset[T]:
        return cast(InsertPermissionRuleset, super().ruleset)
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: InsertionRequest[T]) -> AuthorizationDecision:
        pass