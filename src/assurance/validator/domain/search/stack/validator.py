# src/assurance/validator/domain/search/stack/checker.py

"""
Module: assurance.validator.domain.search.stack.checker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from assurance import ContextValidator, ValidationBundle
from domain import ModelContext
from artifcat import ValidationResult
from util import LoggingLevelRouter

T = TypeVar("T", bound="ModelContext")


class ContextValidator(ContextValidator[T], ABC, Generic[T]):
    """
    Role
        -  Integrity Assurance Worker

    Responsibilities:
        1.  Check that a candidate is the right type of not-null StackContext.
        2.  Run safety checks on any StackSearchContex attributes that are enabled.

    Attributes:
        bundle: ValidationBundle[T]

    Provides:
        - def execute(candidate: Any) -> ValidationResult[T]:

    Super Class:
        ContextIntegrityChecker
    """
    
    def __init__(self, bundle: ValidationBundle[T]):
        """
        Args:
            bundle: ValidationBundle[T]
        """
        super().__init__(bundle=bundle)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[ModelContext]:
        """
        Certify a candidate is a StackContext that is safe to use.
        Args:
            candidate, Any
        Returns:
            ValidationResult[StackContext]
        Raises:
            ContextCheckerException
        """
        pass
    
    
