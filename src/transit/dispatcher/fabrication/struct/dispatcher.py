# src/transit/dispatcher/fabrication/struct/validator.py

"""
Module: transit.dispatcher.fabrication.struct.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast


from artifcat import BuildResult
from assurance import StructValidator
from domain import Struct
from transit import StructCarrier, BuildDispatcher
from util import LoggingLevelRouter

T = TypeVar("T", bound="Struct")

class StructBuildDispatcher(BuildDispatcher[T], ABC, Generic[T]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the StructBuild workflow.

    Attributes:
        validator: StructValidator[T]
        
    Provides:
        -   def execute(self, candidate: Any) -> BuildResult[StructCarrier]

    Super Class:
        BuildDispatcher
    """
    
    def __init__(self, validator: StructValidator[T]):
        """
        Args:
            validator: StructValidator
        """
        super().__init__(validator=validator)


    @property
    def validator(self) -> StructValidator[T]:
        return cast(StructValidator[T], super().validator)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> BuildResult[StructCarrier[T]]:
        """
        Verify a candidate is an EntityCarrier whose payload is safe.
        Args:
            job: Any
        Returns:
            BuildResult[T]
        Raises:
            StructDispatcherException
        """
        pass
    
    
        
        
