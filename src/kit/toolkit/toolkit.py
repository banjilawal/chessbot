# src/kit/toolkit/toolkit.py

"""
Module: kit.toolkit.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from microservice import IdentityService
from assurance.validator import PrimingValidator


class Toolkit:
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Bundles dependencies a worker needs to complete its task.
        2.  Loose Coupling between an operation and its resources.
        3.  Simplify Entry points.

    Attributes:
        identity_service: Optional[IdentityService]
        priming_validator: Optional[PrimingValidator]
        
    Provides:
        
    Super Class:
    """
    _identity_service: Optional[IdentityService]
    _priming_validator: Optional[PrimingValidator]
    
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
        self._priming_validator = priming_validator or PrimingValidator()
        self._identity_service = identity_service or IdentityService()
        
    @property
    def priming_validator(self) -> PrimingValidator:
        return self._priming_validator
    
    @property
    def identity_service(self) -> IdentityService:
        return self._identity_service