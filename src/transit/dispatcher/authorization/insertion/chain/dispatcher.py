# src/transit/dispatcher/authorization/insertion/structure/node/dispatcher.py

"""
Module: transit.dispatcher.authorization.insertion.node.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from authorization import AddNodeRequestAuthorizer
from collection import Chain
from transit.dispatcher import InsertionDispatcher
from domain.structure.searchable.node import Node

from artifcat.report import AuthorizationDecision
from domain.exchange.request import AddNodeRequest

from util import LoggingLevelRouter

T = TypeVar("T", bound="Node")

class AddNodeDispatcher(InsertionDispatcher[Chain], ABC, Generic[T]):
    
    _authorizer: AddNodeRequestAuthorizer[T]
    
    def __init__(self, authorizer: AddNodeRequestAuthorizer[T]):
        """
        Args:
            authorizer: AddNodeRequestAuthorizer[T]
        """
        super().__init__(authorizer=authorizer)
        
    @property
    def authorizer(self) -> AddNodeRequestAuthorizer[T]:
        return cast(AddNodeRequestAuthorizer[T], super().authorizer)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: AddNodeRequest[T]) -> AuthorizationDecision:
        pass