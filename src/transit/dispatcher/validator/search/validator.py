# src/transit/dispatcher/validator/context/validator.py

"""
Module: transit.dispatcher.validator.context.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import ValidationResult
from assurance import ContextValidator, Validator
from domain import Context
from util import LoggingLevelRouter


T = TypeVar("T", bound="Context")


class ContextValidator(Validator[T], ABC, Generic[T]):
    """
    Role
        -  Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a Context instance is safe before use.

    Attributes:
        integrity_checker: ContextChecker[T]
        
    Provides:
        -  execute(self, candidate: Any) -> ValidationResult[T]

    Super Class:
        Validator
    """
    
    def __init__(self, integrity_checker: ContextValidator[T]):
        """
        Args:
            integrity_checker: ContextChecker
        """
        super().__init__(integrity_checker=integrity_checker)
    
    
    @property
    def integrity_checker(self) -> ContextValidator[T]:
        return cast(ContextValidator[T], super().integrity_checker)
   
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[T]:
        """
        Verify a candidate is a safe Context.
        Args:
            candidate: Any
        Returns:
            ValidationResult[T]
        Raises:
            SearchContexValidatorException
        """
        pass
    
    
