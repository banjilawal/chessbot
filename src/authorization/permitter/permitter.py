# src/authorization/permitter/authorizer.py

"""
Module: authorization.permitter.authorizer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from artifcat import Decision
from bootstrap import AuthorizationLoader
from exchange import PermissionRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="PermissionRequest")

class Permitter(ABC, Generic[T]):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Grant permission to perform an activity.

    Attributes:
        loader: AuthorizationLoader[T]
        validation_service: ValidationService[T]
        
    Provides:
        -   def execute(request: T) -> Decision[T]

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
    
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> Decision[T]:
        """
        Grant permission for an activity.
        Args:
            request: T
        Returns:
           Decision[T]
        Raises:
            AuthorizerException
        """
        