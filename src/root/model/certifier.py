# src/certifier/model/validator.py

"""
Module: certifier.model.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, Generic, TypeVar, cast

from root import RootCertifier
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
        RootCertifier
    """
    
    def __init__(self, toolkit: ModelToolkit[T]):
        super().__init__(toolkit=toolkit)
        
    @property
    def toolkit(self) -> ModelToolkit[T]:
        return cast(ModelToolkit[T], super().toolkit)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[T]:
        pass
    
    
