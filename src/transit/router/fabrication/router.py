# src/transit/route/fabrication/router.py

"""
Module: transit.route.fabrication.router
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

from artifcat import BuildResult
from assurance import PrimingValidator
from domain import Blueprint
from transit import Router
from util import LoggingLevelRouter

T = TypeVar("T")


class BuildRouter(Router[BuildResult], ABC, Generic[T]):
    """
    Role
        -   Execution Routing
        
    Responsibilities:
        1.  Routes a Blueprint subclass to the appropriate concrete product assembler.

    Attributes:

    Provides:
            -   def execute(blueprint: Blueprint[T]) -> BuildResult[T]

    Super Class:
        Router
    """
    
    _priming_validator: PrimingValidator
    
    def __init__(
            self,
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        """
        Args:
            priming_validator: Optional[PrimingValidator]
        """
        self._priming_validator = priming_validator
        
    @property
    def priming_validator(self) -> PrimingValidator:
        return self._priming_validator
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: Blueprint[T]) -> BuildResult[T]:
        """
        Routes a Blueprint subclass to its corresponding SubBuilder.

        Args:
             blueprint: Blueprint[T]
        Returns:
            BuildResult[T]
        Raises:
            BuildRouterException
        """
        pass