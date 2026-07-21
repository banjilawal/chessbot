# src/validator/operand/validator.py

"""
Module: validator.operand.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, Generic, TypeVar, cast


from err.root import ToggleRootCertifier
from result import ValidationResult
from toolkit import ToggleToolkit

from validator import Validator

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
            root_certifier: ToggleRootCertifier[T],
    ):
        super().__init__(toolk=toolkit, root_certifier=root_certifier)
        
    
    @property
    def toolkit(self) -> ToggleToolkit:
        return cast(ToggleToolkit[T], self.toolkit)
    
    @property
    def root_certifier(self) -> ToggleRootCertifier[T]:
        return cast(ToggleRootCertifier[T], self.root_certifier)
    
    @abstractmethod
    def execute(self, candidate: Any) -> ValidationResult[T]:
        pass



    
    
        
        
