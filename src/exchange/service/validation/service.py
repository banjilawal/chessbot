# src/exchange/service/validation/service.py

"""
Module: exchange.service.validation.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import ValidationResult
from domain import Blueprint
from exchange import ValidationRequest, ValidationService
from util import LoggingLevelRouter

T = TypeVar("T")

class ValidationService(ABC, Generic[T]):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract the EntityCarrier from a ValidationResponse attribute

    Attributes:
        service: ValidationService[T]

    Provides:
        -   def extract_model(
                    request: ValidationRequest[T]
            ) -> ValidationResult[T]
            
            -   def extract_blueprint(
                    request: ValidationRequest[T]
            ) -> ValidationResult[Blueprint[T]]

    Super Class:
    """
    _service = ValidationService[T]
    
    def __init__(self, service: ValidationService[T]):
        """
        Args:
            service: ValidationService[T]
        """
        self._service = service
        
    @property
    def service(self) ->ValidationService[T]:
        return self._service
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def extract_model(self, request: ValidationRequest[T]) -> ValidationResult[T]:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def extract_model(self, request: ValidationRequest[T]) -> ValidationResult[Blueprint[T]]:
        pass