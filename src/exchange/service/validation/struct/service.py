# src/exchange/server/validation/struct/server.py

"""
Module: exchange.server.validation.struct.server
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
    StructValidationRequest, StructValidationResponder, ValidationService
)
from util import LoggingLevelRouter

T = TypeVar("T", bound="Struct")

class StructValidationServer(ValidationService[T], ABC, Generic[T]):
    """
    Role
        -   Server

    Responsibilities:
        1.  Extract the either:
                -   The Struct
                _   The Blueprint
            from a StructValidationResponse.

    Attributes:
        responder: StructValidationResponder[T]
        
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
        ValidationServer
    """
    
    def __init__(self, responder: StructValidationResponder[T]):
        """
        Args:
            responder: StructValidationResponder[T]
        """
        super().__init__(responder=responder)
    
    @property
    def responder(self) -> StructValidationResponder[T]:
        return cast(StructValidationResponder[T], super().responder)
    
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