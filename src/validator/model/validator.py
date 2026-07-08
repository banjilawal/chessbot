# src/validator/model/validator.py

"""
Module: validator.model.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any

from model import Model
from result import ValidationResult
from toolkit import ModelToolkit
from validator import Validator


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
        Validator
    """
    
    def __init__(self, toolkit: ModelToolkit):
        super().__init__(toolkit=toolkit)
        
    @property
    @abstractmethod
    def toolkit(self) -> ModelToolkit:
        pass
    
    @abstractmethod
    def execute(self, candidate: Any) -> ValidationResult:
        pass
    
    
        
        
