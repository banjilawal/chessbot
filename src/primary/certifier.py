# src/certifier/validator.py

"""
Module: certifier.validator
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
from util import LoggingLevelRouter

T = TypeVar("T",)


class RootCertifier(ABC, Generic[T]):
    """
    Role
        -   Validation Worker
        -   Integrity Assurance

    Responsibilities:
        1.  Ensures a DtoCarrier's data satisfies its model's type and integrity requirements.

    Attributes:
        toolkit: ModelToolkit[T]

    Provides:
        -   execute( carrier: DtoCarrier[T]) -> ValidationResult:

    Super Class:
    """
    _toolkit: ModelToolkit[T]
    _toggle_validator: ToggleValidator
    
    def __init__(
            self,
            toolkit: ModelToolkit[T],
            toggle_validator: ToggleValidator | None = ToggleValidator(),
    ):
        self._toolkit = toolkit
        self._toggle_validator = toggle_validator
        
    @property
    @abstractmethod
    def toolkit(self) -> ModelToolkit[T]:
        return self._toolkit
    
    @property
    def toggle_validator(self) -> ToggleValidator:
        return self._toggle_validator
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult:
        """
            -   Certify a DtoCarrier's data satisfies a model's integrity constraints.

        Action:
            1.  Implement validation tests here.
        Args:
            candidate: Any
        Returns:
            ValidationResult[DtoCarrier[T]]
        Raises:
        """
        pass
    
    
