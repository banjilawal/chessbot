# src/assurance/checker/search/stack/checker.py

"""
Module: assurance.checker.search.stack.checker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from assurance import SearchContextChecker
from domain import StackSearchContext
from artifcat import ValidationResult
from util import LoggingLevelRouter

T = TypeVar("T", bound="StackSearchContext")


class StackContextChecker(SearchContextChecker[T], ABC, Generic[T]):
    """
    Role
        -   Integrity Assurance Worker

    Responsibilities:
        1.  Check that a candidate is the right type of not-null StackSearchContext.
        2.  Run safety checks on any StackSearchContex attributes that are enabled.

    Attributes:
        bundle: SearchValidationBundle[T]

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[T]:

    Super Class:
        SearchContextIntegrityChecker
    """
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[StackSearchContext]:
        """
        Certify a candidate is a StackSearchContext that is safe to use.
        Args:
            candidate, Any
        Returns:
            ValidationResult[StackSearchContext]
        Raises:
            StackContextCheckerException
        """
        pass
    
    
