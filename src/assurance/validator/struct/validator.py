# src/assurance/validator/struct/validator.py

"""
Module: assurance.validator.struct.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import ValidationResult
from assurance import StructValidatorToolkit, Validator
from domain import Struct, StructValidationRequest
from transit import StructCarrier
from util import LoggingLevelRouter

T = TypeVar("T", bound="Struct")


class StructValidator(Validator[T], ABC, Generic[T]):
    """
    Role
        - Integrity Assurance Worker

    Responsibilities:
        1.  Check that a candidate is the right type of not-null EntityCarrier.
        2.  Run safety checks on structs and blueprints inside an EntityCarrier's payload.

    Attributes:
        toolkit: StructValidatorToolkit[T]

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[StructCarrier[T]]:

    Super Class:
        Validator
    """
    
    def __init__(self, toolkit: StructValidatorToolkit[T]):
        """
        Args:
            toolkit: StructValidatorToolkit[T]
        """
        super().__init__(toolkit=toolkit)
    
    @property
    def toolkit(self) -> StructValidatorToolkit[T]:
        return cast(StructValidatorToolkit[T], super().toolkit)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[StructCarrier[T]]:
        """
        Verify the candidate is an EntityCarrier whose payload is safe.
        Args:
            candidate: Any
        Returns:
           ValidationResult[StructCarrier[T]]
        Raises:
            StructValidatorException
        """
        pass
    
    
