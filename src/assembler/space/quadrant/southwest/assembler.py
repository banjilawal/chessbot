# src/assembler/space/quadrant/southwest/assembler.py

"""
Module: assembler.space.quadrant.southwest.assembler
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from blueprint import SouthwestQuadrantBlueprint

from result import BuildResult
from assembler import QuadrantAssembler
from root import SouthwestQuadrant
from util import  LoggingLevelRouter
  
  
class SouthwestQuadrantAssembler(QuadrantAssembler[SouthwestQuadrant]):
    """
    Role
        -   Builder

    Responsibilities:
        1.  Create a SouthwestQuadrant instance from the safe blueprint.

    Attributes:

    Provides:
        -   def execute(self, blueprint: SouthwestQuadrantBlueprint,) -> BuildResult[SouthwestQuadrant]

    Super Class:
        QuadrantAssembler
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
        
        
