# src/authorization/loader/loader.py

"""
Module: authorization.loader.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from artifcat import Decision
from assurance import PrimingValidator
from authorization import AuthorizationLoader
from exchange import CrudPermissionRequest, ValidationService
from microservice import IdentityService
from util import LoggingLevelRouter

T = TypeVar("T", bound="CrudPermissionRequest")

class CrudAuthorizationLoader(AuthorizationLoader[T], ABC, Generic[T]):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Ensure the correct Request type is loaded into a CrudAuthorization module.

    Attributes:
        validation_service: ValidationService

    Provides:
        -   def execute(request: T) -> Decision[T]

    Super Class:
        AuthorizationLoader
    """
    
    def __init__(self, validation_service: ValidationService):
        """
        Args:
            validation_service: ValidationService
        """
        super().__init__(validation_service=validation_service)
    
    @property
    def validation_service(self) -> ValidationService:
        return cast(ValidationService, super().validation_service)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> Decision[T]:
        """
        Checks if the Request is the right type.
        
        Action:
            1.  Send an exception chain in the Decision denial if either;
                    -   the request is null.
                    -   the wrong type.
            2.  Otherwise, send an approval.
        Args:
            request: T
        Returns:
           Decision[T]
        Raises:
            AuthorizationLoaderxception
        """
        pass