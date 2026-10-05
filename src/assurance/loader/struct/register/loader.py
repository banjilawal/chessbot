# src/assurance/load/struct/register/loader.py

"""
Module: assurance.load.struct.register.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import ValidationResult
from assurance import RegisterValidatorToolkit, StructLoader
from domain import Register, RegisterPrimeExtract
from util import LoggingLevelRouter

T = TypeVar("T", bound="Register")

class RegisterLoader(StructLoader[T], ABC, Generic[T]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   RegisterValidationRequest[T]
            -   RegisterCarrier[T]
            -   RegisterBlueprint[T]

    Attributes:

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[RegisterPrimeExtract[T]

    Super Class:
        Loader
    """
    
    def __init__(self, toolkit: RegisterValidatorToolkit[T]):
        """
        Args:
            toolkit: ValidatorToolkit[T]
        """
        super().__init__(toolkit=toolkit)
    
    @property
    def toolkit(self) -> RegisterValidatorToolkit[T]:
        return cast(RegisterValidatorToolkit[T], super().toolkit)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[RegisterPrimeExtract[T]]:
        """
        Extract a safe RegisterBlueprint from the candidate.
        Args:
            candidate: Any
        Returns:
            ValidationResult[RegisterBlueprint[T]]
        Raises:
            RegisterExtractorException
        """
        pass