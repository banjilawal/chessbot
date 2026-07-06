# src/assembler/model/vector/py

"""
Module: assembler.model.vector.assembler
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from result import BuildResult
from operation import Assembler
from util import  LoggingLevelRouter
from model import Vector, VectorBlueprint

class VectorAssembler(Assembler[Vector]):
    NAME = "vector_assembler"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(cls, blueprint: VectorBlueprint,) -> BuildResult[Vector]:
        """
        Assemble the appropriate Vector.

        Args:
            blueprint: VectorBlueprint
        Returns:
            BuildResult[Vector]
        Raises:
        """
        method = f"{cls.__name__}.execute"
        return BuildResult.success(
            Vector(
                x=blueprint.x,
                y=blueprint.y,
            )
        )
        
        
