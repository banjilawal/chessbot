# src/assembler/space/axis/west/assembler.py

"""
Module: assembler.space.axis.west.assembler
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from blueprint import WestAxisBlueprint

from result import BuildResult
from assembler import AxisAssembler
from root import WestAxis
from util import  LoggingLevelRouter
  
  
class WestAxisAssembler(AxisAssembler[WestAxis]):
    """
    Role
        -   Builder

    Responsibilities:
        1.  Create a WestAxis instance from the safe blueprint.

    Attributes:

    Provides:
        -   def execute(self, blueprint: WestAxisBlueprint,) -> BuildResult[WestAxis]

    Super Class:
        AxisAssembler
    """
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: WestAxisBlueprint,) -> BuildResult[WestAxis]:
        """
        Assemble a West from the Blueprint's contents.

        Args:
            blueprint: WestAxisBlueprint
        Returns:
            BuildResult[WestAxis]
        Raises:
        """
        method = f"{self.__class__.__name__}.execute"
        return BuildResult.success(WestAxis(origin=blueprint.origin))
        
        
