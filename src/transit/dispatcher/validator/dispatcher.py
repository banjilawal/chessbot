# src/transit/dispatcher/validator/validator.py

"""
Module: transit.dispatcher.validator.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from assurance import Validator
from artifcat import ValidationResult
from transit import Dispatcher
from util import LoggingLevelRouter


T = TypeVar("T")


class ValidationDispatcher(Dispatcher, ABC, Generic[T]):
    """
    Role
        -  Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure data-holders are safe before they are used or saved.
        
    Attributes:
        integrity_checker: IntegrityChecker[T]
    
    Provides:
        -  def execute(candidate: Any) -> ValidationResult[T]
        
    super Class:
    """
    _integrity_checker: Validator[T]
    
    def __init__(self, integrity_checker: Validator[T], ):
        """
        Args:
            integrity_checker: IntegrityChecker[T]
        """
        self._integrity_checker = integrity_checker
        
    @property
    def integrity_checker(self) -> Validator[T]:
        return self.integrity_checker

    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[T]:
        """
        Verify a candidate is safe to use.
        Args:
            candidate: Any
        Returns:
            ValidationResult[T]
        Raises:
            ValidatorException
        """
        pass
