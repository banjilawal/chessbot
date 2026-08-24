# src/assurance/validator/search/chain/validator.py

"""
Module: assurance.validator.search.chain.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import ValidationResult
from assurance import SearchContextValidator, ChainContextChecker
from domain import ChainSearchContext
from util import LoggingLevelRouter


T = TypeVar("T", bound="ChainSearchContext")


class ChainSearchContextValidator(SearchContextValidator[T], ABC, Generic[T]):
    """
    Role
        -   Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a ChainSearchContext instance is safe before use.

    Attributes:
        integrity_checker: ChainContextChecker[T]
        
    Provides:
        -   execute(self, candidate: Any) -> ValidationResult[T]

    Super Class:
        SearchContextValidator
    """
    
    def __init__(self, integrity_checker: ChainContextChecker[T]):
        """
        Args:
            integrity_checker: ChainContextChecker
        """
        super().__init__(integrity_checker=integrity_checker)
    
    
    @property
    def integrity_checker(self) -> ChainContextChecker[T]:
        return cast(ChainContextChecker[T], super().integrity_checker)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[T]:
        """
        Verify a candidate is a safe ChainSearchContext.
        Args:
            candidate: Any
        Returns:
            ValidationResult[T]
        Raises:
            ChainSearchContexValidatorException
        """
        pass
    
    
