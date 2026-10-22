# src/authorization/checker/valid/applicant.checker.py

"""
Module: authorization.checker.valid.applicant.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TypeVar

from artifcat import Decision
from authorization import ApplicantChecker, Attributable, Checker
from domain import Actor
from exchange import AuthorizationRequest, ValidationService
from util import LoggingLevelRouter

T = TypeVar("T", bound="Actor")

class ValidApplicantChecker(ApplicantChecker[T], ABC):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Verifies an Actor meets minimum safety requirements.

    Attributes:
        validation_service: ValidationService[T]
        
    Provides:
        -   def execute(request: AuthorizationRequest) -> Decision


    Super Class:
        PropertyChecker
    """
    _validation_service: ValidationService[T]
    
    def __init__(self, validation_service: ValidationService[T]):
        """
        Args:
            validation_service: ValidationService[T]
        """
        self._validation_service =validation_service
        
    @property
    def validation_service(self) -> ValidationService[T]:
        return self.validation_service
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: AuthorizationRequest) -> Decision:
        pass