# src/client/validation/client.py

"""
Module: client.validation.client
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import ValidationResult
from client import Client, ValidationRequest
from transit import ValidationDispatcher
from util import LoggingLevelRouter

T = TypeVar("T",)

class ValidatorClient(Client[ValidationResult], ABC, Generic[T]):
    """
    Role
        - Client

    Responsibilities:
        1.  Submit a request to a ValidationDispatcher

    Attributes:
        dispatcher: ValidationDispatcher[T]
        
    Provides:
        -   def submit(request: ValidationRequest[T]) -> ValidationResult

    Super Class:
        Client
    """
    
    def __init__(self, dispatcher: ValidationDispatcher[T]):
        """
        Args:
            dispatcher: ValidationDispatcher[T]
        """
        super().__init__(dispatcher=dispatcher)
        
    @property
    def dispatcher(self) -> ValidationDispatcher[T]:
        return cast(ValidationDispatcher, super().dispatcher)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def submit(self, request: ValidationRequest[T]) -> ValidationResult:
        """
        Args:
            request: ValidationRequest[T]
        Result:
            ValidationResult
        Raises:
            ValidatorClientException
        """
        pass