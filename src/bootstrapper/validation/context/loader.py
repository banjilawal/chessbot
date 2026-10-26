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
from domain import Context, Model
from util import LoggingLevelRouter

T = TypeVar("T", bound="Model")

class ContextValidationLoader(ABC, [T], Generic[T]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   ContextValidationRequest[T]
            -   ContextCarrier[T]
            -   ContextBlueprint[T]

    Attributes:

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[Context[T]

    Super Class:
        Loader
    """
    _toolkit: ValidatorToolkit[T]
    
    def __init__(self, toolkit: ValidatorToolkit[T]):
        """
        Args:
            toolkit: ValidatorToolkit[T]
        """
        self._toolkit = toolkit
    
    @property
    def toolkit(self) -> ValidatorToolkit[T]:
        return self._toolkit
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[Context[T]]:
        """
        Extract a safe ContextBlueprint from the candidate.
        Args:
            candidate: Any
        Returns:
            ValidationResult[ContextBlueprint[T]]
        Raises:
            ContextExtractorException
        """
        pass