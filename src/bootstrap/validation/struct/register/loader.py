# src/bootstrap/validation/struct/register/loader.py

"""
Module: bootstrap.validation.struct.register.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import ValidationResult
from assurance import RegisterLayerToolkit, StructValidationLoader
from domain import Register, Register
from util import LoggingLevelRouter

T = TypeVar("T", bound="Register")

class RegisterValidationLoader(StructValidationLoader[T], ABC, Generic[T]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   RegisterValidationRequest[T]
            -   Register[T]
            -   RegisterBlueprint[T]

    Attributes:

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[T

    Super Class:
        Loader
    """
    
    def __init__(self, toolkit: RegisterLayerToolkit[T]):
        """
        Args:
            toolkit: LayerToolkit[T]
        """
        super().__init__(toolkit=toolkit)
    
    @property
    def toolkit(self) -> RegisterLayerToolkit[T]:
        return cast(RegisterLayerToolkit[T], super().toolkit)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[T]:
        """
        Model a safe RegisterBlueprint from the candidate.
        Args:
            candidate: Any
        Returns:
            ValidationResult[RegisterBlueprint[T]]
        Raises:
            RegisterValidatorException
        """
        pass