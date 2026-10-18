# src/fabrication/contractor/model/encounter/contractor.py

"""
Module: fabrication.contractor.model.encounter.contractor
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from artifcat import BuildResult
from domain import Encounter, EncounterBlueprint
from fabrication import ModelBuildSubcontractor
from util import LoggingLevelRouter

T = TypeVar("T", bound="Encounter")

class EncounterSubcontractor(ModelBuildSubcontractor[T], ABC, Generic[T]):
    """
    Role
        -   Builder
        
    Responsibilities:
        1.  Instantiate an EncounterWarning.

    Attributes:

    Provides:
            -   def execute(blueprint: EncounterBlueprint[T]) -> BuildResult[T]

    Super Class:
        ModelBuildContractor
    """
    
    def __init__(self):
        """
        Args:
        """
        super().__init__()
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: EncounterBlueprint[T]) -> BuildResult[T]:
        """
        Routes an EncounterBlueprint subclass to its corresponding SubBuilder.

        Args:
             blueprint: EncounterBlueprint[T]
        Returns:
            BuildResult[T]
        Raises:
            EncounterSubcontractorException
        """
        pass