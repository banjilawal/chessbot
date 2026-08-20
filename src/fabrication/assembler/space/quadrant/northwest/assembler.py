# src/assembler/space/quadrant/northwesteast/assembler.py

"""
Module: assembler.space.quadrant.northwest.assembler
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from fabrication.blueprint import NorthwestQuadrantBlueprint

from result import BuildResult
from fabrication.assembler import QuadrantAssembler
from assurance.checker import NorthwestQuadrant
from util import  LoggingLevelRouter
  
  
class NorthwestQuadrantAssembler(QuadrantAssembler[NorthwestQuadrant]):
    """
    Role
        -   Builder

    Responsibilities:
        1.  Create a NorthwestQuadrant instance from the safe blueprint.

    Attributes:

    Provides:
        -   def execute(self, blueprint: NorthwestQuadrantBlueprint,) -> BuildResult[NorthwestQuadrant]

    Super Class:
        QuadrantAssembler
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
        
        
