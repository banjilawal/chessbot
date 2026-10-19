# src/authorization/loader/loader.py

"""
Module: authorization.loader.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, TypeVar

from artifcat import ValidationResult
from assurance import PrimingValidator
from exchange import PermissionRequest, ValidationService
from microservice import IdentityService
from util import LoggingLevelRouter

T = TypeVar("T", bound="PermissionRequest")

class AuthorizationLoader(ABC, Generic[T]):
    _priming_validator: PrimingValidator
    _identity_service: IdentityService

    
    def __init__(
            self,
            identity_service: Optional[IdentityService] | None = None,
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        """
        Args:
            identity_service: Optional[IdentityService]
            priming_validator: Optional[PrimingValidator]
        """
        self._identity_service = identity_service or IdentityService()
        self._priming_validator = priming_validator or PrimingValidator()
    
    @property
    def identity_service(self) -> IdentityService:
        return self._identity_service
        
    @property
    def priming_validator(self) -> PrimingValidator:
        return self._priming_validator
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[T]:
        pass