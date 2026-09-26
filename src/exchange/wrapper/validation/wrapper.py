# src/exchange/wrapper/validation/wrapper.py

"""
Module: exchange.wrapper.validation.wrapper
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import ValidationResult
from domain import Blueprint
from exchange import ResponseWrapper, ValidationRequest, ValidationResponder
from util import LoggingLevelRouter

T = TypeVar("T")

class ValidationResponseWrapper(
    ResponseWrapper[ValidationResult],
    ABC,
    Generic[T],
):
    """
    Role
        -   Wrapper

    Responsibilities:
        1.  Extract the EntityCarrier from a ValidationResponse attribute

    Attributes:
        responder: ValidationResponder[T]

    Provides:
        -   def extract_model(
                    request: ValidationRequest[T]
            ) -> ValidationResult[T]
            
            -   def extract_blueprint(
                    request: ValidationRequest[T]
            ) -> ValidationResult[Blueprint[T]]

    Super Class:
        ResponseWrapper
    """
    
    def __init__(self, responder: ValidationResponder[T]):
        """
        Args:
            responder: ValidationResponder[T]
        """
        super().__init__(responder=responder)
        
    @property
    def responder(self) ->ValidationResponder[T]:
        return cast(ValidationResponder[T], super().responder)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def extract_model(
            self,
            request: ValidationRequest[T]
    ) -> ValidationResult[T]:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def extract_model(
            self,
            request: ValidationRequest[T]
    ) -> ValidationResult[Blueprint[T]]:
        pass