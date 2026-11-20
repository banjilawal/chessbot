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
from exchange import ValidationRequest
from transit import ValidationDispatcher
from util import LoggingLevelRouter

T = TypeVar("T")

class ValidationService(ABC, Generic[T]):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract the EntityCarrier from a ValidationResponse attribute

    Attributes:
        dispatcher: ValidationService[T]

    Provides:
        -   def extract_model(
                    request: ValidationRequest[T]
            ) -> ValidationResult[T]
            
            -   def extract_blueprint(
                    request: ValidationRequest[T]
            ) -> ValidationResult[Blueprint[T]]

    Super Class:
    """
    _dispatcher = ValidationDispatcher[T]
    
    def __init__(self, dispatcher: ValidationDispatcher[T]):
        """
        Args:
            dispatcher: ValidationDispatcher[T]
        """
        self._dispatcher = dispatcher
        
    @property
    def dispatcher(self) -> ValidationDispatcher[T]:
        return self._dispatcher
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def extract_model(self, request: ValidationRequest[T]) -> ValidationResult[T]:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def extract_model(self, request: ValidationRequest[T]) -> ValidationResult[Blueprint[T]]:
        pass