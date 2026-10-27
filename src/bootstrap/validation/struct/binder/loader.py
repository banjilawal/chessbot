# src/bootstrap/validation/struct/binder/loader.py

"""
Module: bootstrap.validation.struct.binder.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import ValidationResult
from assurance import BinderLayerToolkit, StructValidationLoader
from domain import ArchetypeBinder
from util import LoggingLevelRouter

T = TypeVar("T", bound="ArchetypeBinder")

class BinderValidationLoader(StructValidationLoader[T], ABC, Generic[T]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   BinderValidationRequest[T]
            -   Binder[T]
            -   BinderBlueprint[T]

    Attributes:

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[T

    Super Class:
        Loader
    """
    
    def __init__(self, toolkit: BinderLayerToolkit[T]):
        """
        Args:
            toolkit: LayerToolkit[T]
        """
        super().__init__(toolkit=toolkit)
    
    @property
    def toolkit(self) -> BinderLayerToolkit[T]:
        return cast(BinderLayerToolkit[T], super().toolkit)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[T]:
        """
        Model a safe BinderBlueprint from the candidate.
        Args:
            candidate: Any
        Returns:
            ValidationResult[BinderBlueprint[T]]
        Raises:
            BinderValidatorException
        """
        pass