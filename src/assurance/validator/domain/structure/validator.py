# src/assurance/validator/validator.py

"""
Module: assurance.validator.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from assurance import DomainObjectValidator, StructureValidationToolkit, ValidationToolkit
from artifcat import ValidationResult
from domain import Blueprint, Structure
from util import LoggingLevelRouter


T = TypeVar("T", bound="Structure")


class StructureValidator(DomainObjectValidator[T], ABC, Generic[T]):
    """
    Role
        - Validator
        - Integrity Assurance
        - Consistency Assurance

    Responsibilities:
        1.  Run integrity checks on an object or its blueprint encapsulated inside their
            EntityCarrier.
        2.  Makes sure objects or their blueprints are safe before they are used.
        3.  Pluggable validation module.

    Attributes:
        toolkit: StructureValidationToolkit[T]

    Provides:
        - def execute(candidate: Any) -> ValidationResult[Blueprint[T]|T]:

    Super Class:
    """
    
    def __init__(self, toolkit: ValidationToolkit[T]):
        """
        Args:
            toolkit: StructureValidationToolkit[T]
        """
        super().__init__(toolkit=toolkit)
    
    |
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[T|Blueprint[T]]:
        """
        Verify the candidate is an EntityCarrier whose payload is safe.
        Args:
            candidate: Any
        Returns:
           ValidationResult[T|Blueprint[T]]
        Raises:
            StructureValidatorException
        """
        pass
    
    
