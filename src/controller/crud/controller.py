# src/controller/crud/controller.py

"""
Module: controller.crud.controller
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Generic, TypeVar

from controller import Controller
from model import Query
from request import DeletionRequest, PopRequest, PushRequest
from result import DeletionResult, InsertionResult, SearchResult
from util import LoggingLevelRouter

T = TypeVar('T')


class CrudController(Controller, Generic[T]):
    pass


    @abstractmethod
    @LoggingLevelRouter.monitor
    def delete(self, request: DeletionRequest) -> DeletionResult[T]:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def pop(self, request: PopRequest) -> DeletionResult[T]:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def push(self, request: PushRequest) -> InsertionResult:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def search(self, query: Query) -> SearchResult:
        pass
    
    
    
    
