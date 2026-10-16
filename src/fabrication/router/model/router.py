# src/transit/route/fabrication/model/router.py

"""
Module: transit.route.fabrication.model.router
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import BuildResult
from domain import Model, ModelBlueprint
from fabrication import BuildRouter
from util import LoggingLevelRouter

T = TypeVar("T", bound="Model")


class ModelBuildRouter(BuildRouter[T], ABC, Generic[T]):
    """
    Role
        -   Execution Routing
        
    Responsibilities:
        1.  Routes a ModelBlueprint subclass to the appropriate concrete
            product assembler.

    Attributes:

    Provides:
            -   def execute(blueprint: ModelBlueprint[T]) -> BuildResult[T]

    Super Class:
        BuildRouter
    """
    
    def __init__(self):
        """
        Args:
        """
        super().__init__()
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: ModelBlueprint[T]) -> BuildResult[T]:
        """
        Routes a ModelBlueprint subclass to its corresponding SubBuilder.

        Args:
             blueprint: Blueprint[T]
        Returns:
            BuildResult[T]
        Raises:
            ModelBuildRouterException
        """
        pass