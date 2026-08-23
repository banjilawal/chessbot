# src/authorization/insertion/node/authorization.py

"""
Module: authorization.insertion.node.authorization
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from authorization import InsertionRequestAuthorizer
from domain.structure.node import Node
from report import AuthorizationDecision
from domain.exchange.request import AddNodeRequest
from toolkit import AddNodeRequestToolkit
from util import LoggingLevelRouter

T = TypeVar("T", bound="Node")

class AddNodeRequestAuthorizer(InsertionRequestAuthorizer, ABC, Generic[T]):
    
    def __init__(self, ruleset: AddNodeRequestToolkit[T]):
        super().__init__(ruleset=ruleset)
        
    @property
    def ruleset(self) -> AddNodeRequestToolkit[T]:
        return cast(AddNodeRequestToolkit[T], super().ruleset)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: AddNodeRequest[T]) -> AuthorizationDecision:
        pass
    
    