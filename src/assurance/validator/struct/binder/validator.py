# src/assurance/validator/struct/binder/validator.py

"""
Module: assurance.validator.struct.binder.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import ValidationResult
from assurance import BinderLoader, BinderValidatorToolkit, StructValidator
from domain import ArchetypeBinder
from transit import BinderCarrier
from util import LoggingLevelRouter

T = TypeVar("T", bound="ArchetypeBinder")


class BinderValidator(StructValidator[T], ABC, Generic[T]):
    """
    Role
        - Integrity Assurance Worker

    Responsibilities:
        1.  Check that a candidate is the right type of not-null EntityCarrier.
        2.  Run safety checks on structs and blueprints inside an EntityCarrier's payload.

    Attributes:
        loader: BinderLoader[T]

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[StructCarrier[T]]:

    Super Class:
        StructValidator
    """
    
    def __init__(self, loader: BinderLoader[T]):
        """
        Args:
            loader: BinderValidatorToolkit[T]
        """
        super().__init__(loader=loader)
    
    @property
    def toolkit(self) -> BinderValidatorToolkit[T]:
        return cast(BinderValidatorToolkit[T], super().toolkit)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[BinderCarrier[T]]:
        """
        Verify the candidate is an EntityCarrier whose payload is safe.
        Args:
            candidate: Any
        Returns:
           ValidationResult[BinderCarrier[T]]
        Raises:
            BinderValidatorException
        """
        pass
    
    
