# src/fabrication/builder/space/axis/south/fabrication/builder.py

"""
Module: fabrication.builder.space.axis.south.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain.metadata.blueprint import SouthAxisBlueprint

from artifcat import BuildResult
from fabrication.builder import AxisBuilder
from assurance.validator import SouthAxis
from util import  LoggingLevelRouter
  
  
class SouthAxisBuilder(AxisBuilder[SouthAxis]):
    """
    Role
        -  Builder

    Responsibilities:
        1.  Create a SouthAxis instance from the safe blueprint.

    Attributes:

    Provides:
        - def execute(self, blueprint: SouthAxisBlueprint,) -> BuildResult[SouthAxis]

    Super Class:
        AxisBuilder
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
        
        
