# src/logic/system/validate/validation.py

"""
Module: logic.system.validate.validation
Author: Banji Lawal
Created: 2025-09-28
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Any

from logic.system import LoggingLevelRouter, ValidationResult

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
        -   execute(rank: Any, *args, **kwargs) -> ValidationResult[T]
        
    super Class:
    """
    
    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any, *args, **kwargs) -> ValidationResult[T]:
        """Implement in subclass."""
        pass
