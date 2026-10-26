# src/bootstrap/validation/context/loader.py

"""
Module: bootstrap.validation.context.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import ValidationResult
from assurance import ValidatorToolkit
from bootstrap import ValidationLoader
from domain import Context, ContextPrimeExtract
from util import LoggingLevelRouter

T = TypeVar("T", bound="Context")

class ContextValidationLoader(ValidationLoader[T], ABC, Generic[T]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   ModelContextValidationRequest[T]
            -   ModelCarrier[T]
            -   ModelBlueprint[T]

    Attributes:

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[ContextPrimeExtract[T]

    Super Class:
        Loader
    """
    
    def __init__(self, toolkit: ValidatorToolkit):
        """
        Args:
            toolkit: ValidatorToolkit[T]
        """
        super().__init__(toolkit=toolkit)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[ContextPrimeExtract[T]]:
        """
        Extract a safe ModelBlueprint from the candidate.
        Args:
            candidate: Any
        Returns:
            ValidationResult[ModelBlueprint[T]]
        Raises:
            ModelExtractorException
        """
        pass