# src/assurance/validator/checker.py

"""
Module: assurance.validator.checker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from artifcat import ValidationResult
from assurance import Loader, ValidatorToolkit
from util import LoggingLevelRouter

T = TypeVar("T",)


class Validator(ABC, Generic[T]):
    """
    Role
        - Validator
        - Integrity Assurance
        - Consistency Assurance

    Responsibilities:
        1.  Run integrity checks on an object or its blueprint encapsulated inside their
            EntityCarrier.
        2.  Makes sure objects or their blueprints are safe before they are used.
        3.  Pluggable validation module.

    Attributes:
        loader: Loader[T]
        loader: ValidatorToolkit[T]

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[Blueprint[T]|T]:

    Super Class:
    """
    _loader: Loader[T]
    
    def __init__(self, loader: Loader[T]):
        """
        Args:
            loader: Loader[T]
            loader: ValidatorToolkit[T]
        """
        self._loader = loader
     
    @property
    def loader(self) -> Loader[T]:
        return self._loader
        
    @property
    def toolkit(self) -> ValidatorToolkit[T]:
        return self._loader.toolkit
    
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
    
    
