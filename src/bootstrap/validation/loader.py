# src/bootstrap/validation/loader.py

"""
Module: bootstrap.validation.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from artifcat import ValidationResult
from assurance import LayerToolkit
from bootstrap import Loader
from domain import PrimeExtract
from util import LoggingLevelRouter

T = TypeVar("T")

class ValidationLoader(Loader[ValidationResult], ABC, Generic[T]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   ValidationRequest[T]
            -   EntityCarrier[T]
            -  Blueprint[T]

    Attributes:
        toolkit: LayerToolkit[T]

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[PrimeExtract[T]]:

    Super Class:
    """
    _toolkit: LayerToolkit[T]
    
    def __init__(self, toolkit: LayerToolkit[T]):
        """
        Args:
            toolkit: toolkit: LayerToolkit[T]
        """
        self._toolkit = toolkit
    
    @property
    def toolkit(self) -> LayerToolkit[T]:
        return self._toolkit
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, bootstrap: Any) -> ValidationResult[PrimeExtract[T]]:
        """
        Extract a safe Extract[T] from the candidate.
        Args:
            bootstrap: Any
        Returns:
            ValidationResult[Extract[T]]
        Raises:
            ValidationLoaderException
        """
        pass