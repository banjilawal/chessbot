# src/validator/operand/validator.py

"""
Module: validator.operand.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, Generic, Optional, TypeVar

from bootstrapper import ToggleValidator
from result import ValidationResult
from toolkit import Toolkit
from validator import Validator

T = TypeVar("T", bound="Operand")


class OperandValidator(Validator[T], Generic[T]):
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
    _toolkit: Optional[Toolkit[T]]
    _toggle_validator: ToggleValidator
    
    def __init__(
            self,
            toolkit: Optional[Toolkit[T]] | None = None,
            toggle_validator: ToggleValidator | None = None,
    ):
        self._toolkit = toolkit
        
    @@property
    def toolkit(self) -> Optional[Toolkit[T]]:
        return self._toolkit
    
    @property
    def toggle_validator(self) -> ToggleValidator:
        return self.toggle_validator
    
    @abstractmethod
    def execute(self, candidate: Any) -> ValidationResult:
        pass

    
    
        
        
