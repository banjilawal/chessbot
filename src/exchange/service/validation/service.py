# src/exchange/server/validation/server.py

"""
Module: exchange.server.validation.server
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import ValidationResult
from domain import Blueprint
from exchange import ValidationRequest, ValidationResponder
from util import LoggingLevelRouter

T = TypeVar("T")

class ValidationService(ABC, Generic[T]):
    """
    Role
        -   Server

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
    """
    _responder = ValidationResponder[T]
    
    def __init__(self, responder: ValidationResponder[T]):
        """
        Args:
            responder: ValidationResponder[T]
        """
        self._responder = responder
        
    @property
    def responder(self) ->ValidationResponder[T]:
        return self._responder
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def extract_model(self, request: ValidationRequest[T]) -> ValidationResult[T]:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def extract_model(self, request: ValidationRequest[T]) -> ValidationResult[Blueprint[T]]:
        pass