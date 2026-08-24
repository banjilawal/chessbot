# src/assembler/space/axis/north/assembler.py

"""
Module: assembler.space.axis.north.assembler
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain.metadata.blueprint import NorthAxisBlueprint

from artifcat import BuildResult
from fabrication.assembler import AxisAssembler
from space import NorthAxis
from util import  LoggingLevelRouter
  
  
class NorthAxisAssembler(AxisAssembler[NorthAxis]):
    """
    Role
        -   Builder

    Responsibilities:
        1.  Create a NorthAxis instance from the safe blueprint.

    Attributes:

    Provides:
        -   def execute(self, blueprint: NorthAxisBlueprint,) -> BuildResult[NorthAxis]

    Super Class:
        AxisAssembler
    """
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: NorthAxisBlueprint,) -> BuildResult[NorthAxis]:
        """
        Assemble a North from the Blueprint's contents.

        Args:
            blueprint: NorthAxisBlueprint
        Returns:
            BuildResult[NorthAxis]
        Raises:
        """
        method = f"{self.__class__.__name__}.execute"
        return BuildResult.success(NorthAxis(origin=blueprint.origin))
        
        
