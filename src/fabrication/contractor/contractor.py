# src/fabrication/contractor/contractor.py

"""
Module: fabrication.contractor.contractor
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

from artifcat import BuildResult
from assurance import PrimingValidator
from domain import Blueprint
from util import LoggingLevelRouter

T = TypeVar("T")


class BuildSubcontractor(ABC, Generic[T]):
    """
    Role
        -   Builder
        
    Responsibilities:
        1.  Instantiate a concrete child of an abstract class.

    Attributes:
        priming_validator: PrimingValidator

    Provides:
            -   def execute(blueprint: Blueprint[T]) -> BuildResult[T]

    Super Class:
    """
    
    _priming_validator: PrimingValidator
    
    def __init__(
            self,
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        """
        Args:
            priming_validator: Optional[PrimingValidator]
        """
        self._priming_validator = priming_validator
        
    @property
    def priming_validator(self) -> PrimingValidator:
        return self._priming_validator
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: Blueprint[T]) -> BuildResult[T]:
        """
        Build a subclass from the subclass Blueprint.

        Args:
             blueprint: Blueprint[T]
        Returns:
            BuildResult[T]
        Raises:
            BuildSubcontractorException
        """
        pass