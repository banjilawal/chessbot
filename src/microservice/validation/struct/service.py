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
    StructValidationRequest, ValidationMicroservice, ValidationService
)
from util import LoggingLevelRouter

T = TypeVar("T", bound="Struct")

class ValidationMicroservice(ValidationService[T], ABC, Generic[T]):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract the either:
                -   The Struct
                _   The Blueprint
            from a StructValidationResponse.

    Attributes:
        dispatcher: ValidationMicroservice[T]
        
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
    
    def __init__(self, dispatcher: ValidationMicroservice[T]):
        """
        Args:
            dispatcher: ValidationMicroservice[T]
        """
        super().__init__(dispatcher=dispatcher)
    
    @property
    def dispatcher(self) -> ValidationMicroservice[T]:
        return cast(ValidationMicroservice[T], super().service)
    
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