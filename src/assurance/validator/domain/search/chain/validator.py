# src/assurance/validator/domain/search/chain/checker.py

"""
Module: assurance.validator.domain.search.chain.checker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from assurance import SearchContextValidator, ValidationBundle
from domain import ChainSearchContext
from artifcat import ValidationResult
from util import LoggingLevelRouter

T = TypeVar("T", bound="ChainSearchContext")


class ChainContextValidator(SearchContextValidator[T], ABC, Generic[T]):
    """
    Role
        -  Integrity Assurance Worker

    Responsibilities:
        1.  Check that a candidate is the right type of not-null ChainSearchContext.
        2.  Run safety checks on any ChainSearchContex attributes that are enabled.

    Attributes:
        bundle: ValidationBundle[T]

    Provides:
        - def execute(candidate: Any) -> ValidationResult[T]:

    Super Class:
        SearchContextIntegrityChecker
    """
    
    def __init__(self, bundle: ValidationBundle[T]):
        """
        Args:
            bundle: ValidationBundle[T]
        """
        super().__init__(bundle=bundle)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[ChainSearchContext]:
        """
        Certify a candidate is a ChainSearchContext that is safe to use.
        Args:
            candidate, Any
        Returns:
            ValidationResult[ChainSearchContext]
        Raises:
            ChainContextCheckerException
        """
        pass
    
    
