# src/authorization/reviewer/reviewer.py

"""
Module: authorization.reviewer.reviewer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

from artifcat import Decision, ValidationResult
from assurance import PrimingValidator
from exchange import ValidationService
from util import LoggingLevelRouter

T = TypeVar("T")

class Reviewer(ABC, Generic[T]):
    """
    Role:
        - Permission Authorization
        - Checklist Runner
        - Integrity Maintenance
        _   Consistency Assurance

    Responsibilities:
        1.  Run safety checks on a .

    Attributes:
        priming_validator: PrimingValidator
        validation_service: ValidationService[T]

    Provides:

    Super Class:
    """
    
    _priming_validator: PrimingValidator
    _validation_service: ValidationService[T]
    
    def __init__(
            self,
            validation_service: ValidationService[T],
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        """
        Args:
            priming_validator: PrimingValidator
            validation_service: ValidationService[T]
        """
        self._validation_service = validation_service
        self._priming_validator = priming_validator or PrimingValidator()
        
    @property
    def priming_validator(self) -> PrimingValidator:
        return self._priming_validator
    
    @property
    def validation_service(self) -> ValidationService[T]:
        return self._validation_service
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: AuthorizationRequest) -> ValidationResult[T]:
        pass
        