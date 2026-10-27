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
from assurance import ContextValidationLoader, ContextLayerToolkit, Validator
from domain import Context
from transit import ContextCarrier
from util import LoggingLevelRouter

T = TypeVar("T", bound="Context")


class ContextValidator(Validator[], ABC, Generic[T]):
    """
    Role
        - Integrity Assurance Worker

    Responsibilities:
        1.  Check that a candidate is the right type of not-null EntityCarrier.
        2.  Run safety checks on contexts and blueprints inside an EntityCarrier's payload.

    Attributes:
        loader: ContextLoader[T]

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[ContextCarrier[T]]:

    Super Class:
        Validator
    """
    
    def __init__(self, loader: ContextValidationLoader[T]):
        """
        Args:
            loader: ContextLoader[T]
        """
        super().__init__(loader=loader)
    
    @property
    def loader(self) -> ContextValidationLoader[T]:
        return cast(ContextValidationLoader[T], super().loader)
    
    @property
    def toolkit(self) -> ContextLayerToolkit[T]:
        return self.toolkit
    
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
    
    
