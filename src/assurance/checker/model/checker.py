# src/assurance/checker/model/checker.py

"""
Module: assurance.checker.model.checker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, Generic, TypeVar

from assurance import IntegrityChecker, ValidationBundle
from model import Model
from result import ValidationResult
from util import LoggingLevelRouter

T = TypeVar("T", bound="Model")


class ModelIntegrityChecker(IntegrityChecker, Generic[T]):
    """
    Role
        -   Validation Worker
        -   Integrity Assurance

    Responsibilities:
        1.  Ensures a DtoCarrier's data satisfies its model's type and integrity requirements.


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
    def bundle(self) -> ValidationBundle[T]:
        return self._bundle
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult:
        pass
    
    
