# src/assurance/load/extractor.py

"""
Module: assurance.load.extractor
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from artifcat import ValidationResult
from assurance import ValidatorToolkit
from domain import PrimeExtract
from util import LoggingLevelRouter

T = TypeVar("T")

class Loader(ABC, Generic[T]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   ValidationRequest[T]
            -   EntityCarrier[T]
            -  Blueprint[T]

    Attributes:
        toolkit: ValidatorToolkit[T]

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[PrimeExtract[T]]:

    Super Class:
    """
    _toolkit: ValidatorToolkit[T]
    
    def __init__(
            self,
            toolkit: ValidatorToolkit[T]
    ):
        """
        Args:
            toolkit: toolkit: Optional[ValidatorToolkit[T]]
        """
        self._toolkit = toolkit
    
    @property
    def toolkit(self) -> ValidatorToolkit[T]:
        return self._toolkit
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[PrimeExtract[T]]:
        """
        Extract a safe Extract[T] from the candidate.
        Args:
            candidate: Any
        Returns:
            ValidationResult[Extract[T]]
        Raises:
            ExtractLoaderException
        """
        pass