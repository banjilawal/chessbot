# src/exchange/wrapper/validation/struct/binder/wrapper.py

"""
Module: exchange.wrapper.validation.struct.binder.wrapper
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import ValidationResult
from domain import Binder, BinderBlueprint
from exchange import (
    BinderValidationRequest, BinderValidationResponder, StructValidationServer,
)
from util import LoggingLevelRouter

T = TypeVar("T", bound="Binder")

class BinderValidationServer(
    StructValidationServer[T],
    ABC,
    Generic[T]
):
    """
    Role
        -   Wrapper

    Responsibilities:
        1.  Extract the either:
                -   The Binder
                _   The Blueprint
            from a BinderValidationResponse.

    Attributes:
        responder: BinderValidationResponder[T]
        
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
        ValidationServer
    """
    
    def __init__(self, responder: BinderValidationResponder[T]):
        """
        Args:
            responder: BinderValidationResponder[T]
        """
        super().__init__(responder=responder)
    
    @property
    def responder(self) -> BinderValidationResponder[T]:
        return cast(BinderValidationResponder[T], super().responder)
    
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