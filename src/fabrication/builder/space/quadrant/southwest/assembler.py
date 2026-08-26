# src/fabrication/builder/space/quadrant/southwest/fabrication/builder.py

"""
Module: fabrication.builder.space.quadrant.southwest.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain.metadata.blueprint import SouthwestQuadrantBlueprint

from artifcat import BuildResult
from fabrication.builder import QuadrantBuilder
from assurance.checker import SouthwestQuadrant
from util import  LoggingLevelRouter
  
  
class SouthwestQuadrantBuilder(QuadrantBuilder[SouthwestQuadrant]):
    """
    Role
        -   Builder

    Responsibilities:
        1.  Create a SouthwestQuadrant instance from the safe blueprint.

    Attributes:

    Provides:
        -   def execute(self, blueprint: SouthwestQuadrantBlueprint,) -> BuildResult[SouthwestQuadrant]

    Super Class:
        QuadrantBuilder
    """
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: SouthwestQuadrantBlueprint,) -> BuildResult[SouthwestQuadrant]:
        """
        Assemble a Southwest from the Blueprint's contents.

        Args:
            blueprint: SouthwestQuadrantBlueprint
        Returns:
            BuildResult[SouthwestQuadrant]
        Raises:
        """
        method = f"{self.__class__.__name__}.execute"
        return BuildResult.success(SouthwestQuadrant(origin=blueprint.origin))
        
        
