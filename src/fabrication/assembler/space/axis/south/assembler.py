# src/assembler/space/axis/south/assembler.py

"""
Module: assembler.space.axis.south.assembler
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from fabrication.blueprint import SouthAxisBlueprint

from result import BuildResult
from fabrication.assembler import AxisAssembler
from assurance.checker import SouthAxis
from util import  LoggingLevelRouter
  
  
class SouthAxisAssembler(AxisAssembler[SouthAxis]):
    """
    Role
        -   Builder

    Responsibilities:
        1.  Create a SouthAxis instance from the safe blueprint.

    Attributes:

    Provides:
        -   def execute(self, blueprint: SouthAxisBlueprint,) -> BuildResult[SouthAxis]

    Super Class:
        AxisAssembler
    """
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: SouthAxisBlueprint,) -> BuildResult[SouthAxis]:
        """
        Assemble a South from the Blueprint's contents.

        Args:
            blueprint: SouthAxisBlueprint
        Returns:
            BuildResult[SouthAxis]
        Raises:
        """
        method = f"{self.__class__.__name__}.execute"
        return BuildResult.success(SouthAxis(origin=blueprint.origin))
        
        
