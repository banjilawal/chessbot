# src/validator/validator.py

"""
Module: validator.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from result import ValidationResult
from toolkit import ModelToolkit, Toolkit
from util import LoggingLevelRouter

T = TypeVar("T")


class Validator(ABC, Generic[T]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner
        
    Naming Conventions:
        -   Workers are named <EntityName>Validator.
        -   Worker modules are named validator.
        -   Exception modules are named transaction.

    Responsibilities:
        1.  Ensure data-holders are safe before they are used or saved.
        
    Attributes:
    
    Provides:
        -   execute(candidate: Any) -> ValidationResult
        
    super Class:
    """
    _toolkit: ModelToolkit[T]
    
    def __init__(self, toolkit: ModelToolkit):
        self._toolkit = toolkit
        
    @property
    @abstractmethod
    def toolkit(self) -> ModelToolkit[T]:
        pass
    

    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any,) -> ValidationResult:
        """Implement in subclass."""
        pass
