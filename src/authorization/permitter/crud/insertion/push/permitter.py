# src/authorization/permitter/crud/insertion/push/permitter.py

"""
Module: authorization.permitter.crud.insertion.push.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import Decision
from authorization import InsertionPermitter
from exchange import PushPermissionRequest
from exchange.service import ValidationService
from util import LoggingLevelRouter

T = TypeVar("T", bound="PushPermissionRequest")

class PushPermitter(InsertionPermitter[T], ABC, Generic[T]):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Issue a decision about a PushPermissionRequest then forward that decision to
            a Pusher.


    Attributes:
        loader: PushAuthorizationLoader[T]
        validation_service: ValidationService

    Provides:
        -   def execute(candidate: Any) -> Decision

    Super Class:
        InsertionPermitter
    """
    
    def __init__(
            self,
            loader: PushAuthorizationLoader[T],
            validation_service: ValidationService,
    ):
        """
        Args:
            loader: PushAuthorizationLoader[T]
            validation_service: ValidationService
        """
        super().__init__(loader=loader, validation_service=validation_service)
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> Decision:
        """
        Grant permission for a stack push.
        
        Args:
            candidate: Any
        Returns:
           Decision
        Raises:
            PushPermitterException
        """
        