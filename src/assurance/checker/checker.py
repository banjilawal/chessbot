# src/assurance/certifier/toggle/assurance/certifier.py

"""
Module: assurance.certifier.toggle.certifier
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from assurance import ValidationBundle
from fabrication.blueprint import Blueprint
from result import ValidationResult
from util import LoggingLevelRouter

T = TypeVar("T",)


class Checker(ABC, Generic[T]):
    """
    Role
        -   Validator
        -   Integrity Assurance
        -   Consistency Assurance

    Responsibilities:
        1.  Run integrity checks on an object or its blueprint encapsulated inside their
            EntityCarrier.
        2.  Makes sure objects or their blueprints are safe before they are used.
        3.  Pluggable validation module.

    Attributes:
        bundle: ValidationBundle[T]

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[Blueprint[T]|T]:

    Super Class:
    """
    _bundle: ValidationBundle[T]
    
    def __init__(self, bundle: ValidationBundle[T]):
        """
        Args:
            bundle: ValidationBundle[T]
        """
        self._bundle = bundle
        
    @property
    def toolkit(self) -> ValidationBundle[T]:
        return self._bundle
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[Blueprint[T]|T]:
        pass
    
    
