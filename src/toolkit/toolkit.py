# src/toolkit/toolkit.py

"""
Module: toolkit.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from integrity import NumberValidator
from microservice import IdentityService
from operation import ValidationBootstrapper

T = TypeVar("T")



class Toolkit(ABC, Generic[T]):
    """
    Role:
        -   Container
        
    Responsibilities:
        1.  Collection of workers and services that are required for a task.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        number_validator: NumberValidator
        identity_service: IdentityService
        validation_bootstrap: ValidationBootstrapper

    Provides:

    Super Class:
    """
    _number_validator: NumberValidator
    _identity_service: IdentityService
    _validation_bootstrapper: ValidationBootstrapper
    
    def __init__(
            self,
            number_validator: NumberValidator | None = None,
            identity_service: IdentityService | None = None,
            validation_bootstrap: ValidationBootstrapper | None = None,
            
    ):
        """
        Args:
            number_validator: NumberValidator
            identity_service: IdentityService
            validation_bootstrap: ValidationBootstrapper
        """
        self._number_validator = number_validator or NumberValidator()
        self._identity_service = identity_service or IdentityService()
        self._validation_bootstrapper = validation_bootstrap or ValidationBootstrapper()
        
        
    @property
    def number_validator(self) -> NumberValidator:
        return self._number_validator
    
    @property
    def identity_service(self) -> IdentityService:
        return self._identity_service

    @property
    def validation_bootstrap(self) -> ValidationBootstrapper:
        return self._validation_bootstrapper