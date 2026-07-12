# src/consistency/checker.py

"""
Module: consistency.checker
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from bootstrapper import PrimingValidator
from operand import EntityCarrier
from result import ValidationResult
from util import LoggingLevelRouter

T = TypeVar("T")


class ConsistencyChecker(ABC, Generic[T]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner
        
    Naming Conventions:
        -   Workers are named <EntityName>Consistency.
        -   Worker modules are named consistency.
        -   Exception modules are named transaction.

    Responsibilities:
        1.  Ensure data-holders are safe before they are used or saved.
        
    Attributes:
        priming_validator: PrimingValidator
    
    Provides:
        -   execute(dto_operand: DtoOperand[T]) -> ValidationResult
        
    super Class:
    """
    _priming_validator: PrimingValidator
    
    def __init__(
            self,
            priming_validator: PrimingValidator | None = PrimingValidator()
    ):
        self._priming_validator = priming_validator
        
    @property
    def priming_validator(self) -> PrimingValidator:
        return self._priming_validator
        

    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, dto_operand: EntityCarrier[T], ) -> ValidationResult:
        """Implement in subclass."""
        pass
