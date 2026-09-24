# src/assurance/validator/structure/register/validator.py

"""
Module: assurance.validator.structure.register.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import ValidationResult
from assurance import RegisterValidatorToolkit, StructureValidator
from domain import Register
from transit import RegisterCarrier
from util import LoggingLevelRouter

T = TypeVar("T", bound="Register")


class RegisterValidator(StructureValidator[T], ABC, Generic[T]):
    """
    Role
        - Integrity Assurance Worker

    Responsibilities:
        1.  Check that a candidate is the right type of not-null EntityCarrier.
        2.  Run safety checks on structures and blueprints inside an EntityCarrier's payload.

    Attributes:
        toolkit: RegisterValidatorToolkit[T]

    Provides:
        - def execute(candidate: Any) -> ValidationResult[StructureCarrier[T]]:

    Super Class:
        StructureValidator
    """
    
    def __init__(self, toolkit: RegisterValidatorToolkit[T]):
        """
        Args:
            toolkit: RegisterValidatorToolkit[T]
        """
        super().__init__(toolkit=toolkit)
    
    @property
    def toolkit(self) -> RegisterValidatorToolkit[T]:
        return cast(RegisterValidatorToolkit[T], super().toolkit)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[RegisterCarrier[T]]:
        """
        Verify the candidate is an EntityCarrier whose payload is safe.
        Args:
            candidate: Any
        Returns:
           ValidationResult[RegisterCarrier[T]]
        Raises:
            RegisterValidatorException
        """
        pass
    
    
