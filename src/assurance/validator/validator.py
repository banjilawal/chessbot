# src/assurance/validator/validator.py

"""
Module: assurance.validator.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from artifcat import ValidationResult
from bootstrap import ValidationLoader
from util import LoggingLevelRouter

T = TypeVar("T",)


class Validator(ABC, Generic[T]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run integrity checks on an object or its blueprint encapsulated inside their
            EntityCarrier.
        2.  Makes sure objects or their blueprints are safe before they are used.
        3.  Pluggable validation module.

    Attributes:
        loader: ValidationLoader[T]

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[Blueprint[T]|T]:

    Super Class:
    """
    _loader: ValidationLoader[T]
    
    def __init__(self, loader: ValidationLoader[T]):
        """
        Args:
            loader: ValidationLoader[T]
        """
        self._loader = loader
     
    @property
    def loader(self) -> ValidationLoader[T]:
        return self._loader
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[T]:
        """
        Verify the candidate is an EntityCarrier whose payload is safe.
        Args:
            candidate: Any
        Returns:
           ValidationResult[T]
        Raises:
            ValidatorException
        """
        pass
    
    
