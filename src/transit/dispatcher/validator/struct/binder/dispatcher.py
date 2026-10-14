# src/transit/dispatcher/validator/struct/binder/validator.py

"""
Module: transit.dispatcher.validator.binder.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from assurance import BinderValidator
from artifcat import ValidationResult
from domain import Binder
from transit import BinderCarrier, StructValidationDispatcher
from util import LoggingLevelRouter

T = TypeVar("T", bound="Binder")

class BinderValidationDispatcher(StructValidationDispatcher[T], ABC, Generic[T]):
    """
    Role
        - Transaction Worker
        - Integrity Maintenance
        - Consistency Assurance
        - Validation Process Owner

    Responsibilities:
        1.  Ensure a Model instance is certified safe, reliable, and consistent before use.

    Attributes:
        validator: BinderValidator[T]
        
    Provides:
        -   def execute(self, candidate: Any) -> ValidationResult

    Super Class:
        Validator
    """
    
    def __init__(self, validator: BinderValidator[T]):
        super().__init__(validator=validator)
    
    @property
    def validator(self) -> BinderValidator:
        return cast(BinderValidator[T], super().validator)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[BinderCarrier[T]]:
        pass
    
        
        
