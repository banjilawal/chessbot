# src/transit/controller/crud/controller.py

"""
Module: transit.controller.crud.controller
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Generic, TypeVar

from transit.controller import Controller
from domain.exchange.request import CollectionDeletionRequest, PopRequest, TokenStackPushRequest
from result import DeletionResult, InsertionResult, SearchResult
from util import LoggingLevelRouter

T = TypeVar('T')


class CrudController(Controller, Generic[T]):
    pass


    @abstractmethod
    @LoggingLevelRouter.monitor
    def delete(self, request: CollectionDeletionRequest) -> DeletionResult[T]:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def pop(self, request: PopRequest) -> DeletionResult[T]:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def push(self, request: TokenStackPushRequest) -> InsertionResult:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def search(self, request: SearchResult) -> SearchResult:
        pass
    
    
    
    
