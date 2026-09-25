# src/transit/dispatcher/validator/model/validator.py

"""
Module: transit.dispatcher.validator.model.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast


from artifcat import ValidationResult
from assurance import ModelValidator
from domain import Model
from transit import ModelCarrier, ValidationDispatcher
from util import LoggingLevelRouter

T = TypeVar("T", bound="Model")

class ModelValidationDispatcher(ValidationDispatcher[T], ABC, Generic[T]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the ModelValidation workflow.

    Attributes:
        validator: ModelValidator[T]
        
    Provides:
        -   def execute(self, candidate: Any) -> ValidationResult[ModelCarrier]

    Super Class:
        ValidationDispatcher
    """
    
    def __init__(self, validator: ModelValidator[T]):
        """
        Args:
            validator: ModelValidator
        """
        super().__init__(validator=validator)


    @property
    def validator(self) -> ModelValidator[T]:
        return cast(ModelValidator[T], super().validator)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[ModelCarrier[T]]:
        """
        Verify a candidate is an EntityCarrier whose payload is safe.
        Args:
            job: Any
        Returns:
            ValidationResult[T]
        Raises:
            ModelDispatcherException
        """
        pass
    
    
        
        
