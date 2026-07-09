# src/certifier/validator.py

"""
Module: certifier.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar


from result import ValidationResult
from toolkit import ModelToolkit
from util import LoggingLevelRouter
from validator import Validator

T = TypeVar("T", bound="Model")


class Certifier(ABC, Generic[T]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a Blueprint instance is certified safe, reliable and consistent before use.

    Attributes:
        toolkit: ModelToolkit

    Provides:
        -   def validate(candidate: Any, toolkit: ModelToolkit[T],) -> ValidationResult[Blueprint[T]]:

    Super Class:
    """
    _toolkit: ModelToolkit[T]
    
    def __init__(self, toolkit: ModelToolkit[T]):
        super().__init__(toolkit=toolkit)
        
    @property
    @abstractmethod
    def toolkit(self) -> ModelToolkit[T]:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any,) -> ValidationResult:
        pass
    
    
