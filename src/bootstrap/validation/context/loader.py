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
from assurance import LayerToolkit
from bootstrap import ValidationLoader
from domain import Context, ContextPrimeExtract
from util import LoggingLevelRouter

T = TypeVar("T", bound="Context")

class ContextValidationLoader(ValidationLoader[T], ABC, Generic[T]):
    """
    Role
        -   Process Bootstrapper

    Responsibilities:
        1.  Run type and null checks on Items requiring Context Validation.

    Attributes:

    Provides:
        -   def execute(item: Any) -> ValidationResult[ContextPrimeExtract[T]

    Super Class:
        Loader
    """
    
    def __init__(self, toolkit: LayerToolkit):
        """
        Args:
            toolkit: LayerToolkit[T]
        """
        super().__init__(toolkit=toolkit)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, bootstrap: Any) -> ValidationResult[ContextPrimeExtract[T]]:
        """
        Extract a safe ModelBlueprint from the candidate.
        Args:
            bootstrap: Any
        Returns:
            ValidationResult[ModelBlueprint[T]]
        Raises:
            ModelExtractorException
        """
        pass