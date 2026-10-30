# src/assurance/validator/context/validator.py

"""
Module: assurance.validator.context.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import ValidationResult
from assurance import Validator
from bootstrap import ContextValidationLoader
from domain import Context
from production import AccountContextValidationManager
from transit import ContextCarrier
from util import LoggingLevelRouter

T = TypeVar("T", bound="Context")


class ContextValidator(Validator[T], ABC, Generic[T]):
    """
    Role
        - Integrity Assurance Worker

    Responsibilities:
        1.  Check that a candidate is the right type of not-null EntityCarrier.
        2.  Run safety checks on contexts and blueprints inside an EntityCarrier's payload.

    Attributes:
        manager: COntextValidationManager[T]

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[ContextCarrier[T]]:

    Super Class:
        Validator
    """
    _manager: AccountContextValidationManager[T]
    
    def __init__(self, manager: AccountContextValidationManager[T]):
        """
        Args:
            manager: AccountContextValidationManager[T]
        """
        super().__init__(loader=manager.loader)
        self._manager = manager
    
    @property
    def loader(self) -> ContextValidationLoader[T]:
        return self.manager.loader
    
    @property
    def manager(self) -> AccountContextValidationManager[T]:
        return self._manager
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[ContextCarrier[T]]:
        """
        Verify the candidate is an EntityCarrier whose payload is safe.
        Args:
            candidate: Any
        Returns:
           ValidationResult[T]
        Raises:
            ContextValidatorException
        """
        pass
    
    
