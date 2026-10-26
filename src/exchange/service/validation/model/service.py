# src/exchange/service/validation/model/service.py

"""
Module: exchange.service.validation.model.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import ValidationResult
from domain import Model, ModelBlueprint
from exchange import (
    ModelValidationRequest, ModelValidationService, ValidationService
)
from util import LoggingLevelRouter

T = TypeVar("T", bound="Model")

class ModelValidationService(ValidationService[T], ABC, Generic[T]):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract the either:
                -   The Model
                _   The Blueprint
            from a ModelValidationResponse.

    Attributes:
        service: ModelValidationService[T]
        
    Provides:
        -   def extract_model(
                    self,
                    request: ModelValidationRequest[T]
            ) -> ValidationResult[T]
            
        -   def extract_blueprint(
                    self,
                    request: ModelValidationRequest[T]
            ) -> ValidationResult[Blueprint[T]]

    Super Class:
        ValidationService
    """
    
    def __init__(self, service: ModelValidationService[T]):
        """
        Args:
            service: ModelValidationService[T]
        """
        super().__init__(service=service)
    
    @property
    def service(self) -> ModelValidationService[T]:
        return cast(ModelValidationService[T], super().service)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def extract_model(
            self,
            request: ModelValidationRequest[T]
    ) -> ValidationResult[T]:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def extract_model(
            self,
            request: ModelValidationRequest[T]
    ) -> ValidationResult[ModelBlueprint[T]]:
        pass