# src/transit/dispatcher/validator/structure/register/validator.py

"""
Module: transit.dispatcher.validator.register.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from assurance import RegisterValidator
from artifcat import ValidationResult
from domain import Register
from transit import RegisterCarrier, StructureValidationDispatcher
from util import LoggingLevelRouter

T = TypeVar("T", bound="Register")

class RegisterValidationDispatcher(StructureValidationDispatcher[T], ABC, Generic[T]):
    """
    Role
        - Transaction Worker
        - Integrity Maintenance
        - Consistency Assurance
        - Validation Process Owner

    Responsibilities:
        1.  Ensure a Model instance is certified safe, reliable, and consistent before use.

    Attributes:
        validator: RegisterValidator[T]
        
    Provides:
        -   def execute(self, candidate: Any) -> ValidationResult

    Super Class:
        Validator
    """
    
    def __init__(self, validator: RegisterValidator[T]):
        super().__init__(validator=validator)
    
    @property
    def validator(self) -> RegisterValidator:
        return cast(RegisterValidator[T], super().validator)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[RegisterCarrier[T]]:
        pass
    
        
        
