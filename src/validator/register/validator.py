# src/validator/register/validator.py

"""
Module: validator.register.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any

from register import Register
from result import ValidationResult
from validator import Validator


class RegisterValidator(Validator[Register]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Validation Process Owner

    Responsibilities:
        1.  Ensure a Register instance is certified safe, reliable and consistent before use.

    Attributes:
        
    Provides:
        -   execute(self, candidate: Any) -> ValidationResult

    Super Class:
        Validator
    """

    
    @abstractmethod
    def execute(self, candidate: Any) -> ValidationResult:
        pass
    
    
        
        
