# src/assurance/loader/loader.py

"""
Module: assurance.loader.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from artifcat import ValidationResult
from assurance import ValidatorToolkit
from domain import Blueprint
from util import LoggingLevelRouter

T = TypeVar("T")

class BlueprintLoader(ABC, Generic[T]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Extract a blueprint from the validation candidate.

    Attributes:
        toolkit: ValidatorToolkit[T]

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[Blueprint[T]]:

    Super Class:
    """
    _toolkit: ValidatorToolkit[T]
    
    def __init__(self, toolkit: ValidatorToolkit[T]):
        """
        Args:
            toolkit: ValidatorToolkit
        """
        self._toolkit = toolkit
    
    @property
    def toolkit(self) -> ValidatorToolkit[T]:
        return self._toolkit
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[Blueprint[T]]:
        """
        Extract a safe Blueprint[T] from the candidate.
        Args:
            candidate: Any
        Returns:
            ValidationResult[Blueprint[T]]
        Raises:
            BlueprintLoaderException
        """
        pass