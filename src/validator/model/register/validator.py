# src/validator/model/register/validator.py

"""
Module: validator.model.register.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any

from model import Model, Register
from result import ValidationResult
from toolkit import RegisterToolkit
from validator import BlueprintPrimingValidator, ModelValidator, Validator


class RegisterValidator(ModelValidator[Register]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Validation Process Owner

    Responsibilities:
        1.  Ensure a Model instance is certified safe, reliable and consistent before use.

    Attributes:
        toolkit: RegisterToolkit
        
    Provides:
        -   execute(self, candidate: Any) -> ValidationResult

    Super Class:
        ModelValidator
    """
    def __init__(self, bootstrapper: RegisterCertifier):
        super().__init__(bootstrapper=bootstrapper)
        
    @property
    @abstractmethod
    def bootstrapper(self) -> RegisterCertifier:
        pass
    
    @abstractmethod
    def execute(self, candidate: Any) -> ValidationResult:
        pass
    
    
        
        
