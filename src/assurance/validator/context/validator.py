# src/assurance/validator/context/validator.py

"""
Module: assurance.validator.context.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import ValidationResult
from assurance import SearchContextChecker, Validator
from domain import SearchContext
from util import LoggingLevelRouter


T = TypeVar("T", bound="SearchContext")


class ContextValidator(Validator[T], ABC, Generic[T]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a Context instance is certified safe, reliable, and consistent before use.

    Attributes:
        integrity_checker: ContextIntegrityChecker[T]
        
    Provides:
        -   execute(self, candidate: Any) -> ValidationResult

    Super Class:
        Validator
    """
    
    def __init__(self, integrity_checker: SearchContextChecker[T]):
        """
        Args:
            integrity_checker: SearchContextChecker
        """
        super().__init__(integrity_checker=integrity_checker)
    
    @property
    def integrity_checker(self) -> SearchContextChecker[T]:
        return cast(SearchContextChecker[T], super().integrity_checker)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[T]:
        pass
    
    
