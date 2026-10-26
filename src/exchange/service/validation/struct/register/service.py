# src/exchange/service/validation/struct/register/service.py

"""
Module: exchange.service.validation.struct.register.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import ValidationResult
from domain import Register, RegisterBlueprint
from exchange import (
    RegisterValidationRequest, RegisterValidationService, StructValidationService,
)
from util import LoggingLevelRouter

T = TypeVar("T", bound="Register")

class RegisterValidationService(
    StructValidationService[T],
    ABC,
    Generic[T]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract the either:
                -   The Register
                _   The Blueprint
            from a RegisterValidationResponse.

    Attributes:
        service: RegisterValidationService[T]
        
    Provides:
        -   def extract_model(
                    self,
                    request: RegisterValidationRequest[T]
            ) -> ValidationResult[T]
            
        -   def extract_blueprint(
                    self,
                    request: RegisterValidationRequest[T]
            ) -> ValidationResult[Blueprint[T]]

    Super Class:
        ValidationService
    """
    
    def __init__(self, service: RegisterValidationService[T]):
        """
        Args:
            service: RegisterValidationService[T]
        """
        super().__init__(service=service)
    
    @property
    def service(self) -> RegisterValidationService[T]:
        return cast(RegisterValidationService[T], super().service)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def extract_model(
            self,
            request: RegisterValidationRequest[T]
    ) -> ValidationResult[T]:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def extract_model(
            self,
            request: RegisterValidationRequest[T]
    ) -> ValidationResult[RegisterBlueprint[T]]:
        pass