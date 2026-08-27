# src/assurance/validator/checker.py

"""
Module: assurance.validator.checker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from assurance import ValidationBundle, Validator
from artifcat import ValidationResult
from domain import DomainDataObject
from util import LoggingLevelRouter


T = TypeVar("T", bound="DomainDataObject")


class DomainObjectValidator(Validator[T], ABC, Generic[T]):
    """
    Role
        -  Validator
        -  Integrity Assurance
        -  Consistency Assurance

    Responsibilities:
        1.  Run integrity checks on an object or its blueprint encapsulated inside their
            EntityCarrier.
        2.  Makes sure objects or their blueprints are safe before they are used.
        3.  Pluggable validation module.

    Attributes:
        bundle: ValidationBundle[T]

    Provides:
        - def execute(candidate: Any) -> ValidationResult[Blueprint[T]|T]:

    Super Class:
    """
    _bundle: ValidationBundle[T]
    
    
    def __init__(self, bundle: ValidationBundle[T]):
        """
        Args:
            bundle: ValidationBundle[T]
        """
        super().__init__(bundle=bundle)
        
        
    @property
    def bundle(self) -> ValidationBundle[T]:
        return cast(ValidationBundle, super().bundle)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[T]:
        """
        Verify the candidate is an EntityCarrier whose payload is safe.
        Args:
            candidate: Any
        Returns:
           ValidationResult[T]
        Raises:
            IntegrityCheckerException
        """
        pass
    
    
