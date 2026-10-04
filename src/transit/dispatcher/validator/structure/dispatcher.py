# src/transit/dispatcher/validator/structure/validator.py

"""
Module: transit.dispatcher.validator.structure.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast


from artifcat import ValidationResult
from assurance import StructureValidator
from domain import Structure
from transit import StructureCarrier, ValidationDispatcher
from util import LoggingLevelRouter

T = TypeVar("T", bound="Structure")

class StructureValidationDispatcher(ValidationDispatcher[T], ABC, Generic[T]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the StructureValidation workflow.

    Attributes:
        validator: StructureValidator[T]
        
    Provides:
        -   def execute(self, candidate: Any) -> ValidationResult[StructureCarrier]

    Super Class:
        ValidationDispatcher
    """
    
    def __init__(self, validator: StructureValidator[T]):
        """
        Args:
            validator: StructureValidator
        """
        super().__init__(validator=validator)


    @property
    def validator(self) -> StructureValidator[T]:
        return cast(StructureValidator[T], super().validator)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[StructureCarrier[T]]:
        """
        Verify a candidate is an EntityCarrier whose payload is safe.
        Args:
            job: Any
        Returns:
            ValidationResult[T]
        Raises:
            StructureDispatcherException
        """
        pass
    
    
        
        
