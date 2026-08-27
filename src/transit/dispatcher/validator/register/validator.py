# src/transit/dispatcher/validator/structure/register/validator.py

"""
Module: transit.dispatcher.validator.register.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, Generic, TypeVar, cast

from assurance import RegisterIntegrityChecker
from artifcat import ValidationResult
from transit import ValidationDispatcher

T = TypeVar("T", bound="Register")

class RegisterValidationDispatcher(ValidationDispatcher, Generic[T]):
    """
    Role
        -  Transaction Worker
        -  Integrity Maintenance
        -  Consistency Assurance
        -  Validation Process Owner

    Responsibilities:
        1.  Ensure a Model instance is certified safe, reliable and consistent before use.

    Attributes:
        integrity_checker: RegisterIntegrityChecker[T]
        
    Provides:
        -  execute(self, candidate: Any) -> ValidationResult

    Super Class:
        Validator
    """
    
    def __init__(self, integrity_checker: [RegisterIntegrityChecker[T]]):
        super().__init__(integrity_checker=integrity_checker)
    
    @property
    def integrity_checker(self) -> RegisterIntegrityChecker:
        return cast(RegisterIntegrityChecker[T], super().integrity_checker)
    
       @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[T]:
        pass
    
        
        
