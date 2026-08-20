# src/assurance/validator/validator.py

"""
Module: assurance.validator.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from assurance.checker import Certifier
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

    Responsibilities:
        1.  Ensure data-holders are safe before they are used or saved.
        
    Attributes:
        certifier: RootCertifier[T]
    
    Provides:
        -   def execute(candidate: Any) -> ValidationResult[T]
        
    super Class:
    """
    _certifier: Certifier[T]
    
    def __init__(self, certifier: Certifier[T],):
        """
        Args:
            certifier: RootCertifier[T]
        """
        self.certifier = certifier
        
    @property
    def certifier(self) -> Certifier[T]:
        return self.certifier

    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[T]:
        """Implement in subclass."""
        pass
