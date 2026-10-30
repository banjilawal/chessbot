# src/transit/dispatcher/validator/context/dispatcher.py

"""
Module: transit.dispatcher.validator.context.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast


from artifcat import ValidationResult
from assurance import ContextValidator
from domain import Context
from transit import ContextCarrier, ValidationDispatcher
from util import LoggingLevelRouter

T = TypeVar("T", bound="Context")

class ContextValidationDispatcher(ValidationDispatcher[T], ABC, Generic[T]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the ContextValidation workflow.

    Attributes:
        validator: ContextValidator[T]
        
    Provides:
        -   def execute(self, candidate: Any) -> ValidationResult[ContextCarrier]

    Super Class:
        ValidationDispatcher
    """
    
    def __init__(self, validator: ContextValidator[T]):
        """
        Args:
            validator: ContextValidator
        """
        super().__init__(validator=validator)


    @property
    def validator(self) -> ContextValidator[T]:
        return cast(ContextValidator[T], super().validator)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[ContextCarrier[T]]:
        """
        Verify a candidate is an EntityCarrier whose payload is safe.
        Args:
            job: Any
        Returns:
            ValidationResult[T]
        Raises:
            ContextDispatcherException
        """
        pass
    
    
        
        
