# src/transit/route/validation/context/router.py

"""
Module: transit.route.validation.context.router
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from artifcat import ValidationResult
from bootstrap import ContextValidationLoader
from domain import Context
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
    
    _loader: ContextValidationLoader
    
    def __init__(self, loader: ContextValidationLoader):
        """
        Args:
            loader: ContextValidationLoader
        """
        super().__init__()
    
    @property
    def toolkit(self) -> ContextValidationLoader:
        return self._loader
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[ContextCarrier[T]]:
        pass