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
from bootstrap import AuthorizationLoader
from exchange import CrudPermissionRequest
from exchange.service import ValidationService
from util import LoggingLevelRouter

T = TypeVar("T", bound="CrudPermissionRequest")

class CrudPermitter(ABC, Generic[T]):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Issue a decision about a CrudPermissionRequest then forward that decision to
            a CrudWorker.

    Attributes:
        loader: AuthorizationLoader[T]

    Provides:
        -   def execute(request: T) -> CrudDecision

    Super Class:
    """
    _loader: AuthorizationLoader[T]
    _validation_service: ValidationService[T]

    def __init__(
            self,
            loader: AuthorizationLoader[T],
            validation_service: ValidationService[T],
    ):
        """
        Args:
            loader: AuthorizationLoader[T]
            validation_service: ValidationService[T]
        """
        self._loader = loader
        self._validation_service = validation_service
        
    @property
    def loader(self) -> AuthorizationLoader[T]:
        return self._loader
    
    @property
    def validation_service(self) -> ValidationService[T]:
        return self._validation_service
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> CrudDecision:
        """
        Grant permission for an activity.
        
        Args:
            request: T
        Returns:
           CrudDecision
        Raises:
            CrudPermitterException
        """
        