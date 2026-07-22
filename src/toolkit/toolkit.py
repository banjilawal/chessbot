# src/toolkit/toolkit.py

"""
Module: toolkit.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from bootstrapper import PrimingValidator, EntityCarrierToggleValidator
from microservice import IdentityService


class Toolkit:
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Bundles dependencies a worker needs to complete its task.
        2.  Loose Coupling between an operation and its resources.
        3.  Simplify Entry points.

    Attributes:
        identity_service: IdentityService
        priming_validator: PrimingValidator
        toggle_validator: ToggleValidator
    Provides:
        
    Super Class:
    """
    _identity_service: IdentityService
    _priming_validator: PrimingValidator
    _toggle_validator: EntityCarrierToggleValidator
    
    def __init__(
            self,
            identity_service: IdentityService  | None= IdentityService(),
            priming_validator: PrimingValidator | None = PrimingValidator(),
            toggle_validator: EntityCarrierToggleValidator | None = EntityCarrierToggleValidator(),
    ):
        """
        Args:
            identity_service: IdentityService
            priming_validator: PrimingValidator
        """
        self._priming_validator = priming_validator
        self._identity_service = identity_service
        self._toggle_validator = toggle_validator
        
    @property
    def priming_validator(self) -> PrimingValidator:
        return self._priming_validator
    
    @property
    def identity_service(self) -> IdentityService:
        return self._identity_service
    
    @property
    def toggle_valiator(self) -> EntityCarrierToggleValidator:
        return self._toggle_validator