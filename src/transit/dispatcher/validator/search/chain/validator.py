# src/transit/dispatcher/validator/search/chain/validator.py

"""
Module: transit.dispatcher.validator.search.chain.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import ValidationResult
from assurance import ContextValidator, ChainContextValidator
from domain import ChainContext
from util import LoggingLevelRouter


T = TypeVar("T", bound="ChainContext")


class ChainContextValidator(ContextValidator[T], ABC, Generic[T]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a ChainContext instance is safe before use.

    Attributes:
        validator: ChainContextChecker[T]
        
    Provides:
        -   def execute(self, candidate: Any) -> ValidationResult[T]

    Super Class:
        ContextValidator
    """
    
    def __init__(self, validator: ChainContextValidator[T]):
        """
        Args:
            validator: ChainContextChecker
        """
        super().__init__(validator=validator)
    
    
    @property
    def validator(self) -> ChainContextValidator[T]:
        return cast(ChainContextValidator[T], super().validator)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[T]:
        """
        Verify a candidate is a safe ChainContext.
        Args:
            candidate: Any
        Returns:
            ValidationResult[T]
        Raises:
            ChainSearchContexValidatorException
        """
        pass
    
    
