# src/assurance/validator/operand/validator.py

"""
Module: assurance.validator.operand.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, Generic, TypeVar, cast


from assurance.checker import ToggleCertifier
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
        toolkit: OperandToolkit

    Provides:
        -   execute(self, candidate: Any) -> ValidationResult

    Super Class:
        OperandValidator
    """
    
    def __init__(
            self,
            toolkit: ToggleToolkit[T],
            root_certifier: ToggleCertifier[T],
    ):
        super().__init__(toolk=toolkit, root_certifier=root_certifier)
        
    
    @property
    def toolkit(self) -> ToggleToolkit:
        return cast(ToggleToolkit[T], self.toolkit)
    
    @property
    def certifier(self) -> ToggleCertifier[T]:
        return cast(ToggleCertifier[T], self.certifier)
    
    @abstractmethod
    def execute(self, candidate: Any) -> ValidationResult[T]:
        pass



    
    
        
        
