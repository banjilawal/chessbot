# src/assurance/validator/model/validator.py

"""
Module: assurance.validator.model.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import ValidationResult
from assurance import ModelValidationToolkit, Validator
from domain import Model
from transit import EntityCarrier
from util import LoggingLevelRouter

T = TypeVar("T", bound="Model")


class ModelValidator(Validator[T], ABC, Generic[T]):
    """
    Role
        - Integrity Assurance Worker

    Responsibilities:
        1.  Check that a candidate is the right type of not-null EntityCarrier.
        2.  Run safety checks on models and blueprints inside an EntityCarrier's payload.

    Attributes:
        toolkit: ModelValidationToolkit[T]

    Provides:
        - def execute(candidate: Any) -> ValidationResult[Blueprint[T]|T]:

    Super Class:
        Validator
    """
    
    def __init__(self, toolkit: ModelValidationToolkit[T]):
        """
        Args:
            toolkit: ValidationToolkit[T]
        """
        super().__init__(toolkit=toolkit)
    
    @property
    def toolkit(self) -> ModelValidationToolkit[T]:
        return cast(ModelValidationToolkit[T], super().toolkit)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[EntityCarrier[T]]:
        """
        Verify the candidate is an EntityCarrier whose payload is safe.
        Args:
            candidate: Any
        Returns:
           ValidationResult[T]
        Raises:
            ValidatorException
        """
        pass
    
    
