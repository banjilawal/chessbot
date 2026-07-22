# src/assembler/model/vector/assembler.py

"""
Module: assembler.model.vector.assembler
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from blueprint import VectorBlueprint
from model import Vector
from result import BuildResult
from assembler import ModelAssembler
from util import  LoggingLevelRouter
  
  
class VectorAssembler(ModelAssembler[Vector]):
    """
    Role
        -   Builder

    Responsibilities:
        1.  Create a Vector instance from the safe blueprint.

    Attributes:

    Provides:
        -   def execute(self, blueprint: VectorBlueprint,) -> BuildResult[Vector]

    Super Class:
        ModelAssembler
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
        
        
