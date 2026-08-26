# src/transit/dispatcher/validator/search/stack/validator.py

"""
Module: transit.dispatcher.validator.search.stack.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import ValidationResult
from assurance import SearchContextValidator, StackContextValidator
from domain import ModelSearchContext
from util import LoggingLevelRouter


T = TypeVar("T", bound="ModelSearchContext")


class StackSearchContextValidator(SearchContextValidator[T], ABC, Generic[T]):
    """
    Role
        -  Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a StackSearchContext instance is safe before use.

    Attributes:
        integrity_checker: StackContextChecker[T]
        
    Provides:
        -  execute(self, candidate: Any) -> ValidationResult[T]

    Super Class:
        SearchContextValidator
    """
    
    def __init__(self, integrity_checker: StackContextValidator[T]):
        """
        Args:
            integrity_checker: StackContextChecker
        """
        super().__init__(integrity_checker=integrity_checker)
    
    
    @property
    def integrity_checker(self) -> StackContextValidator[T]:
        return cast(StackContextValidator[T], super().integrity_checker)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[T]:
        """
        Verify a candidate is a safe StackSearchContext.
        Args:
            candidate: Any
        Returns:
            ValidationResult[T]
        Raises:
            StackSearchContexValidatorException
        """
        pass
    
    
