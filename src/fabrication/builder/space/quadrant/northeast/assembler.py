# src/fabrication/builder/space/quadrant/northeast/fabrication/builder.py

"""
Module: fabrication.builder.space.quadrant.northeast.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain.metadata.blueprint import NortheastQuadrantBlueprint

from artifcat import BuildResult
from fabrication.builder import QuadrantBuilder
from assurance.validator import NortheastQuadrant
from util import  LoggingLevelRouter
  
  
class NortheastQuadrantBuilder(QuadrantBuilder[NortheastQuadrant]):
    """
    Role
        -  Builder

    Responsibilities:
        1.  Create a NortheastQuadrant instance from the safe blueprint.

    Attributes:

    Provides:
        - def execute(self, blueprint: NortheastQuadrantBlueprint,) -> BuildResult[NortheastQuadrant]

    Super Class:
        QuadrantBuilder
    """
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: NortheastQuadrantBlueprint,) -> BuildResult[NortheastQuadrant]:
        """
        Assemble a Northeast from the Blueprint's contents.

        Args:
            blueprint: NortheastQuadrantBlueprint
        Returns:
            BuildResult[NortheastQuadrant]
        Raises:
        """
        method = f"{self.__class__.__name__}.execute"
        return BuildResult.success(NortheastQuadrant(origin=blueprint.origin))
        
        
