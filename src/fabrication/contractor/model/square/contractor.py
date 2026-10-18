# src/fabrication/contractor/model/square/contractor.py

"""
Module: fabrication.contractor.model.square.contractor
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from artifcat import BuildResult
from domain import Square, SquareBlueprint
from fabrication import ModelBuildSubcontractor
from util import LoggingLevelRouter

T = TypeVar("T", bound="Square")

class SquareSubcontractor(ModelBuildSubcontractor[T], ABC, Generic[T]):
    """
    Role
        -   Builder
        
    Responsibilities:
        1.  Instantiate a concrete Square.

    Attributes:

    Provides:
            -   def execute(blueprint: SquareBlueprint[T]) -> BuildResult[T]

    Super Class:
        ModelBuildContractor
    """
    
    def __init__(self):
        """
        Args:
        """
        super().__init__()
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: SquareBlueprint[T]) -> BuildResult[T]:
        """
        Routes a SquareBlueprint subclass to its corresponding SubBuilder.

        Args:
             blueprint: SquareBlueprint[T]
        Returns:
            BuildResult[T]
        Raises:
            SquareSubcontractorException
        """
        pass