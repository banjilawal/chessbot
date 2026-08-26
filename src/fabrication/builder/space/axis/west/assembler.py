# src/fabrication/builder/space/axis/west/fabrication/builder.py

"""
Module: fabrication.builder.space.axis.west.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain.metadata.blueprint import WestAxisBlueprint

from artifcat import BuildResult
from fabrication.builder import AxisBuilder
from assurance.validator import WestAxis
from util import  LoggingLevelRouter
  
  
class WestAxisBuilder(AxisBuilder[WestAxis]):
    """
    Role
        -  Builder

    Responsibilities:
        1.  Create a WestAxis instance from the safe blueprint.

    Attributes:

    Provides:
        -  def execute(self, blueprint: WestAxisBlueprint,) -> BuildResult[WestAxis]

    Super Class:
        AxisBuilder
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
        
        
