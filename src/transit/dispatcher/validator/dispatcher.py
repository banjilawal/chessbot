# src/transit/dispatcher/validator/validator.py

"""
Module: transit.dispatcher.validator.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from assurance import Validator
from artifcat import ValidationResult
from transit import Dispatcher
from util import LoggingLevelRouter


T = TypeVar("T")


class ValidationDispatcher(Dispatcher, ABC, Generic[T]):
    """
    Role
        -   Transport
        -   Forwarding
        -   Integrity Assurance

    Responsibilities:
        1.  Forward jobs to a Validator.
        2.  Send the ValidationResult back to the caller.

    Attributes:
        validator: Validator[T]

    Provides:
        -   def execute(self, candidate: Any) -> ValidationResult[T]

    Super Class:
        Dispatcher
    """
    _validator: Validator[T]
    
    def __init__(self, validator: Validator[T]):
        """
        Args:
            validator: Validator[T]
        """
        self._validator = validator
        
    @property
    def validator(self) -> Validator[T]:
        return self._validator

    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[T]:
        """
        Verify a candidate is safe to use.
        Args:
            job: Any
        Returns:
            ValidationResult[T]
        Raises:
            ModelDispatcherException
        """
        pass
