# src/certifier/validator.py

"""
Module: certifier.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from operand import DtoOperand
from result import ValidationResult
from toolkit import ModelToolkit
from util import LoggingLevelRouter

T = TypeVar("T",)


class RootCertifier(ABC, Generic[T]):
    """
    Role
        -   Validation Worker
        -   Integrity Assurance

    Responsibilities:
        1.  Ensures a DtoOperand's data satisfies its model's type and integrity requirements.

    Attributes:
        toolkit: ModelToolkit[T]

    Provides:
        -   execute( dto_operand: DtoOperand[T]) -> ValidationResult:

    Super Class:
    """
    _toolkit: ModelToolkit[T]
    
    def __init__(self, toolkit: ModelToolkit[T]):
        self._toolkit = toolkit
        
    @property
    @abstractmethod
    def toolkit(self) -> ModelToolkit[T]:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, dto_operand: DtoOperand[T]) -> ValidationResult:
        """
            -   Certify a DtoOperand's data satisfies a model's integrity constraints.

        Action:
            1.  Implement validation tests here.
        Args:
            dto_operand: DtoOperand[T]
        Returns:
            ValidationResult[DtoOperand[T]]
        Raises:
        """
        pass
    
    
