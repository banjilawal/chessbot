# src/fabrication/builder/space/quadrant/northwesteast/fabrication/builder.py

"""
Module: fabrication.builder.space.quadrant.northwest.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain.metadata.blueprint import NorthwestQuadrantBlueprint

from artifcat import BuildResult
from fabrication.builder import QuadrantBuilder
from assurance.validator import NorthwestQuadrant
from util import  LoggingLevelRouter
  
  
class NorthwestQuadrantBuilder(QuadrantBuilder[NorthwestQuadrant]):
    """
    Role
        -  Builder

    Responsibilities:
        1.  Create a NorthwestQuadrant instance from the safe blueprint.

    Attributes:

    Provides:
        - def execute(self, blueprint: NorthwestQuadrantBlueprint,) -> BuildResult[NorthwestQuadrant]

    Super Class:
        QuadrantBuilder
    """
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: NorthwestQuadrantBlueprint,) -> BuildResult[NorthwestQuadrant]:
        """
        Assemble a Northwest from the Blueprint's contents.

        Args:
            blueprint: NorthwestQuadrantBlueprint
        Returns:
            BuildResult[NorthwestQuadrant]
        Raises:
        """
        method = f"{self.__class__.__name__}.execute"
        return BuildResult.success(NorthwestQuadrant(origin=blueprint.origin))
        
        
