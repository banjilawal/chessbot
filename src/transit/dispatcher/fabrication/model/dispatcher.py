# src/transit/dispatcher/fabrication/model/dispatcher.py

"""
Module: transit.dispatcher.fabrication.model.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast


from artifcat import BuildResult
from fabrication import ModelBuilder
from domain import Model
from transit import ModelCarrier, BuildDispatcher
from util import LoggingLevelRouter

T = TypeVar("T", bound="Model")

class ModelBuildDispatcher(BuildDispatcher[T], ABC, Generic[T]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the ModelBuild workflow.

    Attributes:
        builder: ModelBuilder[T]
        
    Provides:
        -   def execute(self, candidate: Any) -> BuildResult[ModelCarrier]

    Super Class:
        BuildDispatcher
    """
    
    def __init__(self, builder: ModelBuilder[T]):
        """
        Args:
            builder: ModelBuilder
        """
        super().__init__(builder=builder)


    @property
    def builder(self) -> ModelBuilder[T]:
        return cast(ModelBuilder[T], super().builder)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> BuildResult[ModelCarrier[T]]:
        """
        Verify a candidate is an EntityCarrier whose payload is safe.
        Args:
            job: Any
        Returns:
            BuildResult[T]
        Raises:
            ModelDispatcherException
        """
        pass
    
    
        
        
