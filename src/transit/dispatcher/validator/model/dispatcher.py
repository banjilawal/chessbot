# src/transit/dispatcher/validator/model/validator.py

"""
Module: transit.dispatcher.validator.model.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, cast


from artifcat import ValidationResult
from domain import Model
from transit import ValidationDispatcher
from util import LoggingLevelRouter


class ModelValidationDispatcher(ValidationDispatcher[Model]):
    """
    Role
        -  Transaction Worker
        -  Integrity Maintenance
        -  Consistency Assurance
        -  Validation Process Owner

    Responsibilities:
        1.  Ensure a Model instance is certified safe, reliable and consistent before use.

    Attributes:
        integrity_checker: ModelIntegrityChecker
        
    Provides:
        -  execute(self, candidate: Any) -> ValidationResult

    Super Class:
        Validator
    """
    
    def __init__(self, integrity_checker: ModelIntegrityChecker):
        """
        Args:
            integrity_checker: ModelIntegrityChecker
        """
        super().__init__(integrity_checker=integrity_checker)


    @property
    def integrity_checker(self) -> ModelIntegrityChecker:
        return cast(ModelIntegrityChecker, super().integrity_checker)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult:
        """
        Verify a candidate is an EntityCarrier whose payload is safe.
        Args:
            candidate: Any
        Returns:
            ValidationResult[T]
        Raises:
            ModelValidatorException
        """
        pass
    
    
        
        
