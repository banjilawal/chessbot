# src/fabrication/builder/toggle/vector/fabrication/builder.py

"""
Module: fabrication.builder.toggle.vector.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from fabrication.builder import ToggleBuilder
from domain.metadata.blueprint.structure.toggle import CartesianToggleBlueprint

from artifcat import BuildResult
from domain.structure.toggle import CartesianToggle
from util import LoggingLevelRouter


class CartesianToggleBuilder(ToggleBuilder[CartesianToggle]):
    """
    Role
        -  Builder

    Responsibilities:
        1.  Create a CartesianToggle instance from the safe blueprint.

    Attributes:

    Provides:
        -  def execute(self, blueprint: CartesianToggleBlueprint,) -> BuildResult[CartesianToggle]

    Super Class:
        ToggleBuilder
    """
    def __init__(self):
        super().__init__()
    
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: CartesianToggleBlueprint,) -> BuildResult[CartesianToggle]:
        """
        Assemble a CartesianToggle from the Blueprint's contents.

        Args:
            blueprint: CartesianToggleBlueprint
        Returns:
            BuildResult[CartesianToggle]
        Raises:
        """
        method = f"{self.__class__.__name__}.execute"
        
        return BuildResult.success(
            CartesianToggleBlueprint(coord=blueprint.coord, vector=blueprint.vector)
        )
    
        
        
