# src/assurance/validator/validator/rootgenerator.py

"""
Module: assurance.validator.root.generator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from artifcat import ValidationResult
from assurance import ProductEnvelope, ValidatorToolkit
from domain import Model
from util import LoggingLevelRouter

T = TypeVar("T", bound="Model")

class RootValidator(ABC, Generic[T]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Runs validation checks on fields in Token superclass.

    Attributes:
        loader: TokenValidatorToolkit
        position_validator: TokenPositionValidator

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[ProductEnvelope]:

    Super Class:
    """
    _loader: ValidatorToolkit[T]
    
    def __init__(self, loader: ValidatorToolkit[T]):
        """
        Args:
            loader: ValidatorToolkit[T]
        """
        self._toolkit = toolkit
        
    @property
    def toolkit(self) -> ValidatorToolkit[T]:
        return self._toolkit

    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(
            self,
            candidate: Any,
    ) -> ValidationResult[ProductEnvelope]:
        pass

    
