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
from exchange import ModelBuildRequest
from fabrication import ModelBuilder
from domain import Model
from transit import ModelCarrier, BuildDispatcher
from util import LoggingLevelRouter

Q = TypeVar("Q", bound="ModelBuildRequest")
W = TypeVar("W", bound="ModelBuilder")

class ModelBuildDispatcher(BuildDispatcher[Q, W], ABC, Generic[Q, W]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the ModelBuild workflow.

    Attributes:
        builder: W
        
    Provides:
        -   def execute(self, candidate: Any) -> BuildResult[ModelCarrier]

    Super Class:
        BuildDispatcher
    """
    
    def __init__(self, worker: W):
        """
        Args:
            worker: ModelBuilder
        """
        super().__init__(worker=worker)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: Q) -> BuildResult:
        """
        Verify a candidate is an EntityCarrier whose payload is safe.
        Args:
            request: Any
        Returns:
            BuildResult
        Raises:
            ModelDispatcherException
        """
        pass
    
    
        
        
