# src/certifier/validator.py

"""
Module: certifier.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, Generic, TypeVar, cast

from bootstrapper import EntityCarrierToggleValidator
from primary import RootCertifier
from result import ValidationResult
from toolkit import ModelToolkit
from util import LoggingLevelRouter

T = TypeVar("T", bound="Model")


class ModelRootCertifier(RootCertifier, Generic[T]):
    """
    Role
        -   Validation Worker
        -   Integrity Assurance

    Responsibilities:
        1.  Ensures a DtoCarrier's data satisfies its model's type and integrity requirements.

    Attributes:
        toolkit: ModelToolkit[T]

    Provides:
        -   execute( carrier: DtoCarrier[T]) -> ValidationResult:

    Super Class:
    """
    
    def __init__(
            self,
            toolkit: ModelToolkit[T],
            model_carrier_validator: EntityCarrierToggleValidator,
    ):
        super().__init__(toolkit=toolkit, model_carrier_validator=model_carrier_validator)

        
    @property
    def toolkit(self) -> ModelToolkit[T]:
        return cast(ModelToolkit[T], self.toolkit)
    
    @property
    def model_carrier_validator(self) -> EntityCarrierToggleValidator:
        return self.model_carrier_validator
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult:
        """
            -   Certify a DtoCarrier's data satisfies a model's integrity constraints.

        Action:
            1.  Implement validation tests here.
        Args:
            candidate: Any
        Returns:
            ValidationResult[DtoCarrier[T]]
        Raises:
        """
        pass
    
    
