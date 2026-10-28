# src/transit/route/validation/context/router.py

"""
Module: transit.route.validation.context.router
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import ValidationResult
from assurance import LayerToolkit
from domain import Context, ContextPrimeExtract
from transit import ContextCarrier, ValidationRouter
from util import LoggingLevelRouter

T = TypeVar("T", bound="Context")


class ContextValidationRouter(ValidationRouter[T], ABC, Generic[T]):
    """
    Role
        -   Execution Routing
        
    Responsibilities:
        1.  Routes a Blueprint subclass to the appropriate concrete product assembler.

    Attributes:

    Provides:

    Super Class:
        ValidationRouter[T]
    """
    
    _toolkit: LayerToolkit
    
    def __init__(self, toolkit: LayerToolkit):
        """
        Args:
            toolkit: LayerToolkit
        """
        super().__init__()
    
    @property
    def toolkit(self) -> LayerToolkit:
        return self._toolkit
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, prime_extract: ContextPrimeExtract[T]) -> ValidationResult[ContextCarrier[T]]:
        pass