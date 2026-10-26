# src/authorization/loader/loader.py

"""
Module: authorization.loader.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

from artifcat import Decision
from assurance import PrimingValidator
from exchange import PermissionRequest, ValidationService
from microservice import IdentityService
from util import LoggingLevelRouter

T = TypeVar("T", bound="PermissionRequest")

class AuthorizationLoader(ABC, Generic[T]):
    """
    Role:
        -   Loader, Bootstrapper

    Responsibilities:
        1.  Run type and validation checks on the item before handing off
            to the Permitter for additional processing.

    Attributes:
        identity_service: IdentityService
        priming_validator: PrimingValidator
        validation_service: ValidationService

    Provides:
        -   def execute(request: T) -> Decision[T]

    Super Class:
    """

    _identity_service: IdentityService
    _priming_validator: PrimingValidator
    _validation_service: ValidationService
    
    def __init__(
            self,
            validation_service: ValidationService,
            identity_service: Optional[IdentityService] | None = None,
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        """
        Args:
            validation_service: ValidationService
            identity_service: Optional[IdentityService]
            priming_validator: Optional[PrimingValidator]
        """
        self._validation_service = validation_service
        self._identity_service = identity_service or IdentityService()
        self._priming_validator = priming_validator or PrimingValidator()
    
    @property
    def identity_service(self) -> IdentityService:
        return self._identity_service
        
    @property
    def priming_validator(self) -> PrimingValidator:
        return self._priming_validator
    
    @property
    def validation_service(self) -> ValidationService:
        return self._validation_service
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, target: T) -> Decision[T]:
        """
        Checks if the Request is the right type.
        
        Action:
            1.  Send an exception chain in the Decision denial if either;
                    -   the request is null.
                    -   the wrong type.
            2.  Otherwise, send an approval.
        Args:
            target: T
        Returns:
           Decision[T]
        Raises:
            AuthorizationLoaderException
        """
        pass