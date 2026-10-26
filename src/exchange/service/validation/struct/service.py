# src/exchange/service/validation/struct/service.py

"""
Module: exchange.service.validation.struct.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import ValidationResult
from domain import Struct, StructBlueprint
from exchange import (
    StructValidationRequest, StructValidationService, ValidationService
)
from util import LoggingLevelRouter

T = TypeVar("T", bound="Struct")

class StructValidationService(ValidationService[T], ABC, Generic[T]):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract the either:
                -   The Struct
                _   The Blueprint
            from a StructValidationResponse.

    Attributes:
        service: StructValidationService[T]
        
    Provides:
        -   def extract_model(
                    self,
                    request: StructValidationRequest[T]
            ) -> ValidationResult[T]
            
        -   def extract_blueprint(
                    self,
                    request: StructValidationRequest[T]
            ) -> ValidationResult[Blueprint[T]]

    Super Class:
        ValidationService
    """
    
    def __init__(self, service: StructValidationService[T]):
        """
        Args:
            service: StructValidationService[T]
        """
        super().__init__(service=service)
    
    @property
    def service(self) -> StructValidationService[T]:
        return cast(StructValidationService[T], super().service)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def extract_model(
            self,
            request: StructValidationRequest[T]
    ) -> ValidationResult[T]:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def extract_model(
            self,
            request: StructValidationRequest[T]
    ) -> ValidationResult[StructBlueprint[T]]:
        pass