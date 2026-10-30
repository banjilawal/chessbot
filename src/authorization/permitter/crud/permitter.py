# src/authorization/permitter/crud/permitter.py

"""
Module: authorization.permitter.crud.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import CrudDecision
from authorization import Permitter
from bootstrap import CrudAuthorizationLoader
from exchange import CrudPermissionRequest
from exchange.service import ValidationService
from util import LoggingLevelRouter

T = TypeVar("T", bound="CrudPermissionRequest")

class CrudPermitter(Permitter[T], ABC, Generic[T]):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Issue a decision about a CrudPermissionRequest then forward that decision to
            a CrudWorker.

    Attributes:
        loader: CrudAuthorizationLoader[T]
        validation_service: ValidationService[T]

    Provides:
        -   def execute(request: T) -> CrudDecision

    Super Class:
        Permitter
    """

    def __init__(
            self,
            loader: CrudAuthorizationLoader[T],
            validation_service: ValidationService[T],
    ):
        """
        Args:
            loader: CrudAuthorizationLoader[T]
            validation_service: ValidationService[T]
        """
        super().__init__(loader=loader, validation_service=validation_service)
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> CrudDecision:
        """
        Grant permission for a CRUD activity.
        Args:
            request: T
        Returns:
           CrudDecision
        Raises:
            CrudPermitterException
        """
        