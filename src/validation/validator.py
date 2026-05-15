# src/validation/operation.py

"""
Module: validation.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from result import ValidationResult
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
        -   execute(rank: Any, *args, **kwargs) -> ValidationResult[T]
        
    super Class:
    """
    DOMAIN: str = "Validation"
    
    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any, *args, **kwargs) -> ValidationResult[T]:
        """Implement in subclass."""
        pass
