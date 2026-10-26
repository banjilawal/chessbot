# src/exchange/service/validation/struct/binder/service.py

"""
Module: exchange.service.validation.struct.binder.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import ValidationResult
from domain import ArchetypeBinder, BinderBlueprint
from exchange import (
    BinderValidationRequest, BinderValidationService, StructValidationService,
)
from util import LoggingLevelRouter

T = TypeVar("T", bound="ArchetypeBinder")

class BinderValidationService(
    StructValidationService[T], ABC, Generic[T]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract the either:
                -   The Binder
                _   The Blueprint
            from a BinderValidationResponse.

    Attributes:
        service: BinderValidationService[T]
        
    Provides:
        -   def extract_model(
                    self,
                    request: BinderValidationRequest[T]
            ) -> ValidationResult[T]
            
        -   def extract_blueprint(
                    self,
                    request: BinderValidationRequest[T]
            ) -> ValidationResult[Blueprint[T]]

    Super Class:
        ValidationService
    """
    
    def __init__(self, service: BinderValidationService[T]):
        """
        Args:
            service: BinderValidationService[T]
        """
        super().__init__(service=service)
    
    @property
    def service(self) -> BinderValidationService[T]:
        return cast(BinderValidationService[T], super().service)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def extract_model(
            self,
            request: BinderValidationRequest[T]
    ) -> ValidationResult[T]:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def extract_model(
            self,
            request: BinderValidationRequest[T]
    ) -> ValidationResult[BinderBlueprint[T]]:
        pass