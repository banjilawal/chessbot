# src/transit/dispatcher/fabrication/search/stack/validator.py

"""
Module: transit.dispatcher.fabrication.search.stack.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import BuildResult
from assurance import ContextValidator, ContextValidator
from domain import ModelContext
from util import LoggingLevelRouter


T = TypeVar("T", bound="ModelContext")


class StackContextValidator(ContextValidator[T], ABC, Generic[T]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a StackContext instance is safe before use.

    Attributes:
        validator: ContextChecker[T]
        
    Provides:
        -   def execute(self, candidate: Any) -> BuildResult[T]

    Super Class:
        ContextValidator
    """
    
    def __init__(self, validator: ContextValidator[T]):
        """
        Args:
            validator: ContextChecker
        """
        super().__init__(validator=validator)
    
    
    @property
    def validator(self) -> ContextValidator[T]:
        return cast(ContextValidator[T], super().validator)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> BuildResult[T]:
        """
        Verify a candidate is a safe StackContext.
        Args:
            candidate: Any
        Returns:
            BuildResult[T]
        Raises:
            StackSearchContexValidatorException
        """
        pass
    
    
