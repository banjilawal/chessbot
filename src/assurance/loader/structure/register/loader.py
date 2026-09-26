# src/assurance/loader/structure/register/loader.py

"""
Module: assurance.loader.structure.register.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import ValidationResult
from assurance import BlueprintLoader, RegisterValidationToolkit
from domain import Register, RegisterBlueprint
from util import LoggingLevelRouter

T = TypeVar("T", bound="Register")

class RegisterBlueprintLoader(BlueprintLoader[T], ABC, Generic[T]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Extract a RegisterBlueprint from the validation candidate.

    Attributes:
        toolkit: RegisterValidationToolkit[T]

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[RegisterBlueprint[T]]:

    Super Class:
        BlueprintLoader
    """
    
    def __init__(self, toolkit: RegisterValidationToolkit[T]):
        """
        Args:
            toolkit: RegisterValidationToolkit[T]
        """
        super().__init__(toolkit=toolkit)
    
    @property
    def toolkit(self) -> RegisterValidationToolkit[T]:
        return cast(RegisterValidationToolkit[T], super().toolkit)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[RegisterBlueprint[T]]:
        """
        Extract a safe RegisterBlueprint from the candidate.
        Args:
            candidate: Any
        Returns:
            ValidationResult[RegisterBlueprint[T]]
        Raises:
            RegisterBlueprintLoaderException
        """
        pass