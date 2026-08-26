# src/fabrication/builder/model/vector/fabrication/builder.py

"""
Module: fabrication.builder.model.vector.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain.metadata.blueprint import VectorBlueprint
from domain.model import Vector
from artifcat import BuildResult
from fabrication.builder import ModelBuilder
from util import  LoggingLevelRouter
  
  
class VectorBuilder(ModelBuilder[Vector]):
    """
    Role
        -   Builder

    Responsibilities:
        1.  Create a Vector instance from the safe blueprint.

    Attributes:

    Provides:
        -   def execute(self, blueprint: VectorBlueprint,) -> BuildResult[Vector]

    Super Class:
        ModelBuilder
    """
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: VectorBlueprint,) -> BuildResult[Vector]:
        """
        Assemble a Vector from the Blueprint's contents.

        Args:
            blueprint: VectorBlueprint
        Returns:
            BuildResult[Vector]
        Raises:
        """
        method = f"{self.__class__.__name__}.execute"
        return BuildResult.success(Vector(x=blueprint.x, y=blueprint.y))
        
        
