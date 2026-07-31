# src/assembler/space/axis/east/assembler.py

"""
Module: assembler.space.axis.east.assembler
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from blueprint import EastAxisBlueprint

from result import BuildResult
from assembler import AxisAssembler
from geometry.space import EastAxis
from util import  LoggingLevelRouter
  
  
class EastAxisAssembler(AxisAssembler[EastAxis]):
    """
    Role
        -   Builder

    Responsibilities:
        1.  Create a EastAxis instance from the safe blueprint.

    Attributes:

    Provides:
        -   def execute(self, blueprint: EastAxisBlueprint,) -> BuildResult[EastAxis]

    Super Class:
        AxisAssembler
    """
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: EastAxisBlueprint,) -> BuildResult[EastAxis]:
        """
        Assemble a East from the Blueprint's contents.

        Args:
            blueprint: EastAxisBlueprint
        Returns:
            BuildResult[EastAxis]
        Raises:
        """
        method = f"{self.__class__.__name__}.execute"
        return BuildResult.success(EastAxis(origin=blueprint.origin))
        
        
