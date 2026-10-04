# src/exchange/wrapper/validation/struct/register/wrapper.py

"""
Module: exchange.wrapper.validation.struct.register.wrapper
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import ValidationResult
from domain import Register, RegisterBlueprint
from exchange import (
    RegisterValidationRequest, RegisterValidationResponder, StructValidationResponseWrapper,
)
from util import LoggingLevelRouter

T = TypeVar("T", bound="Register")

class RegisterValidationResponseWrapper(
    StructValidationResponseWrapper[T],
    ABC,
    Generic[T]
):
    """
    Role
        -   Wrapper

    Responsibilities:
        1.  Extract the either:
                -   The Register
                _   The Blueprint
            from a RegisterValidationResponse.

    Attributes:
        responder: RegisterValidationResponder[T]
        
    Provides:
        -   def extract_register(
                    self,
                    request: RegisterValidationRequest[T]
            ) -> ValidationResult[T]
            
        -   def extract_blueprint(
                    self,
                    request: RegisterValidationRequest[T]
            ) -> ValidationResult[Blueprint[T]]

    Super Class:
        ValidationResponseWrapper
    """
    
    def __init__(self, responder: RegisterValidationResponder[T]):
        """
        Args:
            responder: RegisterValidationResponder[T]
        """
        super().__init__(responder=responder)
    
    @property
    def responder(self) -> RegisterValidationResponder[T]:
        return cast(RegisterValidationResponder[T], super().responder)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def extract_register(
            self,
            request: RegisterValidationRequest[T]
    ) -> ValidationResult[T]:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def extract_register(
            self,
            request: RegisterValidationRequest[T]
    ) -> ValidationResult[RegisterBlueprint[T]]:
        pass