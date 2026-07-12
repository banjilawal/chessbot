# src/toolkit/toolkit.py

"""
Module: toolkit.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from bootstrapper import PrimingValidator
from microservice import IdentityService


class Toolkit:
    """
    Role:
        -   Dependency Container
        -   Dynamic Dependency Provider
        
    Responsibilities:
        1.  Aggregates workers and services an entity requires for its tasks.
        2.  Separates dependencies from data objects in operation calls.
        3.  Simplifies entry points.

    Attributes:
        identity_service: IdentityService
        priming_validator: PrimingValidator
    
    Provides:
        
    Super Class:
    """
    _identity_service: IdentityService
    _priming_validator: PrimingValidator
    
    def __init__(
            self,
            identity_service: IdentityService  | None= IdentityService(),
            priming_validator: PrimingValidator | None = PrimingValidator(),
    ):
        """
        Args:
            identity_service: IdentityService
            priming_validator: PrimingValidator
        """
        self._priming_validator = priming_validator
        self._identity_service = identity_service
        
    @property
    def priming_validator(self) -> PrimingValidator:
        return self._priming_validator
    
    @property
    def identity_service(self) -> IdentityService:
        return self._identity_service