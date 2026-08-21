# src/assurance/validator/model/validator.py

"""
Module: assurance.validator.model.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any

from assurance import Validator
from model import Model
from result import ValidationResult


class ModelValidator(Validator[Model]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Validation Process Owner

    Responsibilities:
        1.  Ensure a Model instance is certified safe, reliable and consistent before use.

    Attributes:
        toolkit: ModelToolkit
        
    Provides:
        -   execute(self, candidate: Any) -> ValidationResult

    Super Class:
    """
    _integrity_checker: IntegrityChecker
    
    def __init__(self, integrity_checker: IntegrityChecker):
        self._integrity_checker = integrity_checker

    @property
    @abstractmethod
    def integrity_checker(self) -> IntegrityChecker:
        pass
    
    @abstractmethod
    def execute(self, candidate: Any) -> ValidationResult:
        pass
    
    
        
        
