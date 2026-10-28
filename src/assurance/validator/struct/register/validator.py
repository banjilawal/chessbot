# src/assurance/validator/struct/register/validator.py

"""
Module: assurance.validator.struct.register.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import ValidationResult
from assurance import RegisterValidationLoader, RegisterLayerToolkit, StructValidator
from domain import Register
from transit import RegisterCarrier
from util import LoggingLevelRouter

T = TypeVar("T", bound="Register")


class RegisterValidator(StructValidator[T], ABC, Generic[T]):
    """
    Role
        - Integrity Assurance Worker

    Responsibilities:
        1.  Check that a candidate is the right type of not-null EntityCarrier.
        2.  Run safety checks on structs and blueprints inside an EntityCarrier's payload.

    Attributes:
        loader: RegisterLoader[T]

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[StructCarrier[T]]:

    Super Class:
        StructValidator
    """
    
    def __init__(self, loader: RegisterValidationLoader[T]):
        """
        Args:
            loader: RegisterLayerToolkit[T]
        """
        super().__init__(loader=loader)
    
    @property
    def toolkit(self) -> RegisterLayerToolkit[T]:
        return cast(RegisterLayerToolkit[T], super().toolkit)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, item: Any) -> ValidationResult[RegisterCarrier[T]]:
        """
        Verify the candidate is an EntityCarrier whose payload is safe.
        Args:
            item: Any
        Returns:
           ValidationResult[RegisterCarrier[T]]
        Raises:
            RegisterValidatorException
        """
        pass
    
    
