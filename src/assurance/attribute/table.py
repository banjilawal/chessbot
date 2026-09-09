# src/assurance/attrribute/handler.py

"""
Module: assurance.attrribute.handler
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar

from assurance import PrimingValidator
from domain import Model
from microservice import IdentityService

T = TypeVar("T", bound="Model")


class HelperTable(ABC, Generic[T]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validators a Model needs for its attributes.

    Attributes:
        identity_service: IdentityService
        primin_validator: PrimingValidator

    Provides:

    Super Class:
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