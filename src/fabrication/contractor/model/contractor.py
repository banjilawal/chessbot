# src/fabrication/contractor/model/contractor.py

"""
Module: fabrication.contractor.model.contractor
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import BuildResult
from domain import Model, ModelBlueprint
from fabrication import BuildSubcontractor
from util import LoggingLevelRouter

T = TypeVar("T", bound="Model")


class ModelBuildSubcontractor(BuildSubcontractor[T], ABC, Generic[T]):
    """
    Role
        -   Builder
        
    Responsibilities:
        1.  Instantiate a concrete child of an abstract Model.

    Attributes:

    Provides:
            -   def execute(blueprint: ModelBlueprint[T]) -> BuildResult[T]

    Super Class:
        BuildContractor
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
            ModelBuildSubcontractorException
        """
        pass