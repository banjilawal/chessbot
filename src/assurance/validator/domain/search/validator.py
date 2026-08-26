# src/assurance/validator/domain/structure/validatror.py

"""
Module: assurance.validator.domain.structure.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import ValidationResult
from assurance import Validator, ValidationBundle
from domain import SearchContext
from util import LoggingLevelRouter

T = TypeVar("T", bound="SearchContext")


class SearchContextValidator(Validator, ABC, Generic[T]):
    """
    Role
        -  Integrity Assurance Worker

    Responsibilities:
        1.  Check that a candidate is the right type of not-null SearchContext.
        2.  Run safety checks on any SearchContex attributes that are enabled.

    Attributes:
        bundle: ValidationBundle[T]

    Provides:
        -  def execute(candidate: Any) -> ValidationResult[T]:

    Super Class:
        IntegrityChecker
    """
    
    def __init__(self, bundle: ValidationBundle[T]):
        """
        Args:
            bundle: ValidationBundle[T]
        """
        super().__init__(bundle=bundle)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[T]:
        """
        Verify the candidate is a SearchContext safe to use.
        Args:
            candidate: Any
        Returns:
           ValidationResult[T]
        Raises:
            SearchContextCheckerException
        """
        pass
    
    
