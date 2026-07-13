# src/validator/operand/validator.py

"""
Module: validator.operand.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, TypeVar

from bootstrapper import ToggleValidator
from result import ValidationResult
from toolkit import Toolkit
from validator import Validator

T = TypeVar("T", bound="Operand")



class ChooserValidator(Validator[T]):
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
    _toolkit: Toolkit
    _toggle_validator: ToggleValidator
    
    def __init__(
            self,
            toolkit: Toolkit,
            toggle_validator: ToggleValidator | None = ToggleValidator(),
    ):
        self._toolkit = toolkit
        self._toggle_validator = toggle_validator
        
    
    @property
    def toolkit(self) -> Toolkit:
        return self._toolkit
    
    @property
    def toggle_validator(self) -> ToggleValidator:
        return self._toggle_validator
    
    @abstractmethod
    def execute(self, candidate: Any) -> ValidationResult:
        pass



    
    
        
        
