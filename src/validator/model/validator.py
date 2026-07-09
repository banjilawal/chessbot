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
from validator import Certifier, Validator


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
    _bootstrapper: Certifier
    
    def __init__(self, bootstrapper: Certifier):
        self._bootstrapper = bootstrapper

    @property
    @abstractmethod
    def bootstrapper(self) -> Certifier:
        pass
    
    @abstractmethod
    def execute(self, candidate: Any) -> ValidationResult:
        pass
    
    
        
        
