# src/transit/dispatcher/validator/struct/validator.py

"""
Module: transit.dispatcher.validator.struct.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast


from artifcat import ValidationResult
from assurance import StructValidator
from domain import Struct
from transit import StructCarrier, ValidationDispatcher
from util import LoggingLevelRouter

T = TypeVar("T", bound="Struct")

class StructValidationDispatcher(ValidationDispatcher[T], ABC, Generic[T]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the StructValidation workflow.

    Attributes:
        validator: StructValidator[T]
        
    Provides:
        -   def execute(self, candidate: Any) -> ValidationResult[StructCarrier]

    Super Class:
        ValidationDispatcher
    """
    
    def __init__(self, validator: StructValidator[T]):
        """
        Args:
            validator: StructValidator
        """
        super().__init__(validator=validator)


    @property
    def validator(self) -> StructValidator[T]:
        return cast(StructValidator[T], super().validator)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[StructCarrier[T]]:
        """
        Verify a candidate is an EntityCarrier whose payload is safe.
        Args:
            job: Any
        Returns:
            ValidationResult[T]
        Raises:
            StructDispatcherException
        """
        pass
    
    
        
        
