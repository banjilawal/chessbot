# src/fabrication/builder/space/axis/east/fabrication/builder.py

"""
Module: fabrication.builder.space.axis.east.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain.metadata.blueprint import EastAxisBlueprint

from artifcat import BuildResult
from fabrication.builder import AxisBuilder
from space import EastAxis
from util import  LoggingLevelRouter
  
  
class EastAxisBuilder(AxisBuilder[EastAxis]):
    """
    Role
        -   Builder

    Responsibilities:
        1.  Create a EastAxis instance from the safe blueprint.

    Attributes:

    Provides:
        -   def execute(self, blueprint: EastAxisBlueprint,) -> BuildResult[EastAxis]

    Super Class:
        AxisBuilder
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
        
        
