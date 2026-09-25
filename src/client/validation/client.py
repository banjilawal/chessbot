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
from client import Client
from domain import Request
from transit import ValidationDispatcher
from util import LoggingLevelRouter

T = TypeVar("T", bound="Request")

class ValidatorClient(Client[ValidationResult], ABC, Generic[T]):
    """
    Role
        - Client

    Responsibilities:
        1.  Submit a request to a ValidationDispatcher

    Attributes:
        dispatcher: ValidationDispatcher
        
    Provides:
        -   def submit(request: Request[T]) -> ValidationResult

    Super Class:
        Client
    """
    
    def __init__(self, dispatcher: ValidationDispatcher):
        """
        Args:
            dispatcher: Dispatcher[T]
        """
        super().__init__(dispatcher=dispatcher)
        
    @property
    def dispatcher(self) -> ValidationDispatcher:
        return cast(ValidationDispatcher, super().dispatcher)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def submit(self, request: Request[T]) -> ValidationResult:
        """
        Args:
            request: Request[T]
        Result:
            ValidationResult
        Raises:
            ValidatorClientException
        """
        pass