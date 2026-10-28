# src/assurance/validator/struct/validator.py

"""
Module: assurance.validator.struct.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import ValidationResult
from assurance import StructValidationLoader, StructLayerToolkit, Validator
from domain import Struct
from transit import StructCarrier
from util import LoggingLevelRouter

T = TypeVar("T", bound="Struct")


class StructValidator(Validator[T], ABC, Generic[T]):
    """
    Role
        - Integrity Assurance Worker

    Responsibilities:
        1.  Check that a candidate is the right type of not-null EntityCarrier.
        2.  Run safety checks on structs and blueprints inside an EntityCarrier's payload.

    Attributes:
        loader: StructLoader[T]

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[StructCarrier[T]]:

    Super Class:
        Validator
    """
    
    def __init__(self, loader: StructValidationLoader[T]):
        """
        Args:
            loader: StructLayerToolkit[T]
        """
        super().__init__(loader=loader)
    
    @property
    def loader(self) -> StructValidationLoader[T]:
        return cast(StructValidationLoader[T], super().loader)
    
    @property
    def toolkit(self) -> StructLayerToolkit[T]:
        return self.loader.toolkit
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, item: Any) -> ValidationResult[StructCarrier[T]]:
        """
        Verify the candidate is an EntityCarrier whose payload is safe.
        Args:
            item: Any
        Returns:
           ValidationResult[StructCarrier[T]]
        Raises:
            StructValidatorException
        """
        pass
    
    
