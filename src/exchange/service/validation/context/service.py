# src/exchange/service/validation/context/service.py

"""
Module: exchange.service.validation.context.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import ValidationResult
from domain import Context, ContextBlueprint
from exchange import (
    ContextValidationRequest, ContextValidationService, ContextValidationService
)
from util import LoggingLevelRouter

T = TypeVar("T", bound="Context")

class ContextValidationService(ContextValidationService[T], ABC, Generic[T]):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract the either:
                -   The Context
                _   The Blueprint
            from a ContextValidationResponse.

    Attributes:
        responder: ContextValidationService[T]
        
    Provides:
        -   def extract_context(
                    self,
                    request: ContextValidationRequest[T]
            ) -> ValidationResult[T]
            
        -   def extract_blueprint(
                    self,
                    request: ContextValidationRequest[T]
            ) -> ValidationResult[Blueprint[T]]

    Super Class:
        ContextValidationService
    """
    
    def __init__(self, responder: ContextValidationService[T]):
        """
        Args:
            responder: ContextValidationService[T]
        """
        super().__init__(responder=responder)
    
    @property
    def responder(self) -> ContextValidationService[T]:
        return cast(ContextValidationService[T], super().service)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def extract_context(
            self,
            request: ContextValidationRequest[T]
    ) -> ValidationResult[T]:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def extract_context(
            self,
            request: ContextValidationRequest[T]
    ) -> ValidationResult[ContextBlueprint[T]]:
        pass