# src/authorization/permitter/crud/insertion/permitter.py

"""
Module: authorization.permitter.crud.insertion.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import Decision
from authorization import CrudPermitter
from exchange import InsertionPermissionRequest
from exchange.service import ValidationService
from util import LoggingLevelRouter

T = TypeVar("T", bound="InsertionPermissionRequest")

class InsertionPermitter(CrudPermitter[T], ABC, Generic[T]):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Issue a decision about an InsertionPermissionRequest then forward
            that decision an Inserter.

    Attributes:
        loader: CrudAuthorizationLoader[T]
        validation_service: ValidationService

    Provides:
        -   def execute(candidate: Any) -> Decision

    Super Class:
        CrudPermitter
    """
    
    def __init__(
            self,
            loader: InsertionAuthorizationLoader[T],
            validation_service: ValidationService,
    ):
        """
        Args:
            loader: InsertionAuthorizationLoader[T],
            validation_service: ValidationService,
        """
        super().__init__(loader=loader, validation_service=validation_service)
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> Decision:
        """
        Grant permission for an activity.
        
        Args:
            candidate: Any
        Returns:
           Decision
        Raises:
            InsertionPermitterException
        """
        