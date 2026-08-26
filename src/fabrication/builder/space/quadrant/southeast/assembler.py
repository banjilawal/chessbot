# src/fabrication/builder/space/quadrant/southeast/fabrication/builder.py

"""
Module: fabrication.builder.space.quadrant.southeast.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain.metadata.blueprint import SoutheastQuadrantBlueprint

from artifcat import BuildResult
from fabrication.builder import QuadrantBuilder
from assurance.checker import SoutheastQuadrant
from util import  LoggingLevelRouter
  
  
class SoutheastQuadrantBuilder(QuadrantBuilder[SoutheastQuadrant]):
    """
    Role
        -   Builder

    Responsibilities:
        1.  Create a SoutheastQuadrant instance from the safe blueprint.

    Attributes:

    Provides:
        -   def execute(self, blueprint: SoutheastQuadrantBlueprint,) -> BuildResult[SoutheastQuadrant]

    Super Class:
        QuadrantBuilder
    """
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: SoutheastQuadrantBlueprint,) -> BuildResult[SoutheastQuadrant]:
        """
        Assemble a Southeast from the Blueprint's contents.

        Args:
            blueprint: SoutheastQuadrantBlueprint
        Returns:
            BuildResult[SoutheastQuadrant]
        Raises:
        """
        method = f"{self.__class__.__name__}.execute"
        return BuildResult.success(SoutheastQuadrant(origin=blueprint.origin))
        
        
