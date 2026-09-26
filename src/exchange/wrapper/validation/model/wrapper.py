# src/exchange/wrapper/validation/model/wrapper.py

"""
Module: exchange.wrapper.validation.model.wrapper
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
    ModelValidationRequest, ModelValidationResponder, ValidationResponseWrapper
)
from util import LoggingLevelRouter

T = TypeVar("T", bound="Model")

class ModelValidationResponseWrapper(
    ValidationResponseWrapper[T],
    ABC,
    Generic[T]
):
    """
    Role
        -   Wrapper

    Responsibilities:
        1.  Extract the either:
                -   The Model
                _   The Blueprint
            from a ModelValidationResponse.

    Attributes:
        responder: ModelValidationResponder[T]
        
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
        ValidationResponseWrapper
    """
    
    def __init__(self, responder: ModelValidationResponder[T]):
        """
        Args:
            responder: ModelValidationResponder[T]
        """
        super().__init__(responder=responder)
    
    @property
    def responder(self) -> ModelValidationResponder[T]:
        return cast(ModelValidationResponder[T], super().responder)
    
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