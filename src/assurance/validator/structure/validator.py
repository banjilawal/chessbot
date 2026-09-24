# src/assurance/validator/structure/validator.py

"""
Module: assurance.validator.structure.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import ValidationResult
from assurance import StructureValidatorToolkit, Validator
from domain import Structure, StructureValidationRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="Structure")


class StructureValidator(Validator[T], ABC, Generic[T]):
    """
    Role
        - Integrity Assurance Worker

    Responsibilities:
        1.  Check that a candidate is the right type of not-null EntityCarrier.
        2.  Run safety checks on structures and blueprints inside an EntityCarrier's payload.

    Attributes:
        toolkit: StructureValidationToolkit[T]

    Provides:
        - def execute(candidate: Any) -> ValidationResult[Blueprint[T]|T]:

    Super Class:
        Validator
    """
    
    def __init__(self, toolkit: StructureValidatorToolkit[T]):
        """
        Args:
            toolkit: ValidationToolkit[T]
        """
        super().__init__(toolkit=toolkit)
    
    @property
    def toolkit(self) -> StructureValidatorToolkit[T]:
        return cast(StructureValidatorToolkit[T], super().toolkit)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(
            self,
            candidate: StructureValidationRequest
    ) -> ValidationResult[T]:
        """
        Verify the candidate is an EntityCarrier whose payload is safe.
        Args:
            candidate: ValidationRequest[T]
        Returns:
           ValidationResult[T]
        Raises:
            ValidatorException
        """
        pass
    
    
