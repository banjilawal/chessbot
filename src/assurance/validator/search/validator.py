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
from assurance import StackSearchContextChecker, Validator
from domain import StackSearchContext
from util import LoggingLevelRouter


T = TypeVar("T", bound="StackSearchContext")


class StackSearchContextValidator(Validator[T], ABC, Generic[T]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a StackSearchContext instance is certified safe, reliable, 
            and consistent before use.

    Attributes:
        integrity_checker: StackSearchContextChecker[T]
        
    Provides:
        -   execute(self, candidate: Any) -> ValidationResult[T]

    Super Class:
        Validator
    """
    
    def __init__(self, integrity_checker: StackSearchContextChecker[T]):
        """
        Args:
            integrity_checker: StackSearchContextChecker
        """
        super().__init__(integrity_checker=integrity_checker)
    
    @property
    def integrity_checker(self) -> StackSearchContextChecker[T]:
        return cast(StackSearchContextChecker[T], super().integrity_checker)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[T]:
        pass
    
    
