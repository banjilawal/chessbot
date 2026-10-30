# src/authorization/permitter/crud/search/permitter.py

"""
Module: authorization.permitter.crud.search.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import Decision
from authorization import CrudPermitter
from bootstrap import CrudAuthorizationLoader
from exchange import SearchPermissionRequest
from exchange.service import ValidationService
from util import LoggingLevelRouter

T = TypeVar("T", bound="SearchPermissionRequest")

class SearchPermitter(CrudPermitter[T], ABC, Generic[T]):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Issue a decision about a SearchPermissionRequest then forward
            that decision to a SearchWorker.

    Attributes:
        loader: CrudAuthorizationLoader[T]

    Provides:
        -   def execute(request: T) -> Decision[T]

    Super Class:
        CrudPermitter
    """
    
    def __init__(self, loader: CrudAuthorizationLoader[T]):
        """
        Args:
            loader: CrudAuthorizationLoader[T]
        """
        super().__init__(loader=loader)
    
    @property
    def loader(self) -> CrudAuthorizationLoader[T]:
        return cast(CrudAuthorizationLoader[T], super().loader)
    
    @property
    def validation_service(self) -> ValidationService[T]:
        return cast(ValidationService[T], super().validation_service)
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> Decision[T]:
        """
        Grant permission for an activity.
        
        Args:
            request: T
        Returns:
           Decision[T]
        Raises:
            SearchPermitterException
        """
        