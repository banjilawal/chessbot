# src/bootstrap/authorization/loader.py

"""
Module: bootstrap.authorization.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, TypeVar

from artifcat import Decision
from assurance import PrimingValidator
from bootstrap import Loader
from exchange import PermissionRequest
from microservice import IdentityService
from util import LoggingLevelRouter

T = TypeVar("T", bound="PermissionRequest")

class AuthorizationLoader(Loader[T], ABC, Generic[T]):
    """
    Role:
        -   Loader, Bootstrap

    Responsibilities:
        1.  Run basic type and validation checks on items entering the permitting process.

    Attributes:
        identity_service: IdentityService
        priming_validator: PrimingValidator

    Provides:
        -   def execute(candidate: Any) -> Decision

    Super Class:
        Loader
    """
    _identity_service: IdentityService
    _priming_validator: PrimingValidator
    
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
    def execute(self, candidate: Any) -> Decision:
        """
        Checks a
        
        Action:
            1.  Send an exception chain in the Decision denial if either;
                    -   the request is null.
                    -   the wrong type.
            2.  Otherwise, send an approval.
        Args:
            candidate: Any
        Returns:
           Decision
        Raises:
            AuthorizationLoaderException
        """
        pass