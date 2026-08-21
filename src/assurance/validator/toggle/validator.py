# src/assurance/validator/operand/validator.py

"""
Module: assurance.validator.operand.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, Generic, TypeVar, cast


from assurance import ToggleIntegrityChecker
from result import ValidationResult
from toolkit import ToggleToolkit

from assurance.validator import Validator

T = TypeVar("T", bound="Toggle")



class ToggleValidator(Validator, Generic[T]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Validation Process Owner

    Responsibilities:
        1.  Ensure a Operand instance is certified safe, reliable and consistent before use.

    Attributes:
        integrity_checker: OperandToolkit

    Provides:
        -   execute(self, candidate: Any) -> ValidationResult

    Super Class:
        OperandValidator
    """
    
    def __init__(
            self,
            integrity_checker: ToggleToolkit[T],
            integrity_checker: ToggleIntegrityChecker[T],
    ):
        super().__init__(toolk=toolkit, integrity_checker=integrity_checker)
        
    
    @property
    def toolkit(self) -> ToggleIntegrity_Checker:
        return cast(ToggleToolkit[T], self.toolkit)
    
    @property
    def integrity_checker(self) -> ToggleIntegrityChecker[T]:
        return cast(ToggleIntegrityChecker[T], self.integrity_checker)
    
       @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[T]:
        pass



    
    
        
        
