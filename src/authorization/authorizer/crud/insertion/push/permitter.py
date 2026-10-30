# src/authorization/permitter/crud/insertion/push/permitter.py

"""
Module: authorization.permitter.crud.insertion.push.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import Decision
from authorization import InsertionPermitter
from bootstrap import CrudAuthorizationLoader
from exchange import PushPermissionRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="PushPermissionRequest")

class PushPermitter(InsertionPermitter[T], ABC, Generic[T]):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Issue a decision about a PushPermissionRequest then forward that decision to
            an InsertionWorker.

    Attributes:

    Provides:
        -   def execute(request: T) -> Decision[T]

    Super Class:
        InsertionPermitter
    """
    
    def __init__(self,  loader: CrudAuthorizationLoader[T]):
        """
        Args:
            loader: CrudAuthorizationLoader[T]
        """
        super().__init__(loader=loader)
    
    @property
    def loader(self) -> CrudAuthorizationLoader[T]:
        return cast(CrudAuthorizationLoader[T], super().loader)
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> Decision[T]:
        """
        Grant permission for a stack push.
        
        Args:
            request: T
        Returns:
           Decision[T]
        Raises:
            PushPermitterException
        """
        