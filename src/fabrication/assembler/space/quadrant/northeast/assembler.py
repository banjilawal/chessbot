# src/assembler/space/quadrant/northeast/assembler.py

"""
Module: assembler.space.quadrant.northeast.assembler
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain.metadata.blueprint import NortheastQuadrantBlueprint

from result import BuildResult
from fabrication.assembler import QuadrantAssembler
from assurance.checker import NortheastQuadrant
from util import  LoggingLevelRouter
  
  
class NortheastQuadrantAssembler(QuadrantAssembler[NortheastQuadrant]):
    """
    Role
        -   Builder

    Responsibilities:
        1.  Create a NortheastQuadrant instance from the safe blueprint.

    Attributes:

    Provides:
        -   def execute(self, blueprint: NortheastQuadrantBlueprint,) -> BuildResult[NortheastQuadrant]

    Super Class:
        QuadrantAssembler
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
        
        
