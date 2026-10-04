# src/exchange/wrapper/validation/structure/wrapper.py

"""
Module: exchange.wrapper.validation.structure.wrapper
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import ValidationResult
from domain import Structure, StructureBlueprint
from exchange import (
    StructureValidationRequest, StructureValidationResponder, ValidationResponseWrapper
)
from util import LoggingLevelRouter

T = TypeVar("T", bound="Structure")

class StructureValidationResponseWrapper(
    ValidationResponseWrapper[T],
    ABC,
    Generic[T]
):
    """
    Role
        -   Wrapper

    Responsibilities:
        1.  Extract the either:
                -   The Structure
                _   The Blueprint
            from a StructureValidationResponse.

    Attributes:
        responder: StructureValidationResponder[T]
        
    Provides:
        -   def extract_model(
                    self,
                    request: StructureValidationRequest[T]
            ) -> ValidationResult[T]
            
        -   def extract_blueprint(
                    self,
                    request: StructureValidationRequest[T]
            ) -> ValidationResult[Blueprint[T]]

    Super Class:
        ValidationResponseWrapper
    """
    
    def __init__(self, responder: StructureValidationResponder[T]):
        """
        Args:
            responder: StructureValidationResponder[T]
        """
        super().__init__(responder=responder)
    
    @property
    def responder(self) -> StructureValidationResponder[T]:
        return cast(StructureValidationResponder[T], super().responder)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def extract_model(
            self,
            request: StructureValidationRequest[T]
    ) -> ValidationResult[T]:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def extract_model(
            self,
            request: StructureValidationRequest[T]
    ) -> ValidationResult[StructureBlueprint[T]]:
        pass