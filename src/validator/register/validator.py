# src/validator/register/validator.py

"""
Module: validator.register.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, Generic, TypeVar

from err.root import RegisterRootCertifier
from result import ValidationResult
from validator import Validator

T = TypeVar("T", bound="Register")

class RegisterValidator(Validator, Generic[T]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Validation Process Owner

    Responsibilities:
        1.  Ensure a Model instance is certified safe, reliable and consistent before use.

    Attributes:
        root_certifier: RegisterRootCertifier[T]
        
    Provides:
        -   execute(self, candidate: Any) -> ValidationResult

    Super Class:
        Validator
    """
    _root_certifier: RegisterRootCertifier[T]
    
    def __init__(self, root_certifier: RegisterRootCertifier[T]):
        self._root_certifier = root_certifier
        # super().__init__(root_certifier=root_certifier)
    
    @property
    def root_certifier(self) -> RegisterRootCertifier:
        return self._root_certifier
    
    # @property
    # def root_certifier(self) -> RegisterRootCertifier:
    #     return cast(RegisterRootCertifier[T], self.root_certifier)
    
    @abstractmethod
    def execute(self, candidate: Any) -> ValidationResult[T]:
        pass
    
        
        
