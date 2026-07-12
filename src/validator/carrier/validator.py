# src/validator/carrier/__init__.py

"""
Module: validator.carrier.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from bootstrapper import ToggleValidator
from carrier import EntityCarrier
from result import ValidationResult
from toolkit import ModelToolkit
from validator import Validator

T = TypeVar("T", bound="EntityCarrier")


class CarrierValidator(ABC, Generic[T]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Validation Process Owner

    Responsibilities:
        1.  Ensure a Model instance is certified safe, reliable and consistent before use.

    Attributes:
        toolkit: ModelToolkit[T]
        
    Provides:
        -   execute(self, candidate: Any) -> ValidationResult

    Super Class:
        ModelValidator
    """
    _bootstrapper: ToggleValidator
    _toolkit: ModelToolkit[T]
    
    def __init__(
            self,
            toolkit: ModelToolkit,
            bootstrapper: ToggleValidator | None = ToggleValidator(),
    ):
        self._bootstrapper = bootstrapper
        
    @property
    def bootstrapper(self) -> ToggleValidator:
        return self._bootstrapper
    
    @property
    def toolkit(self) -> ModelToolkit[T]:
        return self._toolkit
    
    @abstractmethod
    def execute(self, candidate: Any) -> ValidationResult:
        pass
    
    
        
        
