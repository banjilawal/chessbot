# src/transit/dispatcher/fabrication/struct/register/dispatcher.py

"""
Module: transit.dispatcher.fabrication.register.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from fabrication import RegisterBuilder
from artifcat import BuildResult
from domain import Register
from transit import RegisterCarrier, StructBuildDispatcher
from util import LoggingLevelRouter

T = TypeVar("T", bound="Register")

class RegisterBuildDispatcher(StructBuildDispatcher[T], ABC, Generic[T]):
    """
    Role
        - Transaction Worker
        - Integrity Maintenance
        - Consistency Assurance
        - Build Process Owner

    Responsibilities:
        1.  Ensure a Model instance is certified safe, reliable, and consistent before use.

    Attributes:
        builder: RegisterBuilder[T]
        
    Provides:
        -   def execute(self, candidate: Any) -> BuildResult

    Super Class:
        Builder
    """
    
    def __init__(self, builder: RegisterBuilder[T]):
        super().__init__(builder=builder)
    
    @property
    def builder(self) -> RegisterBuilder:
        return cast(RegisterBuilder[T], super().builder)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> BuildResult[RegisterCarrier[T]]:
        pass
    
        
        
