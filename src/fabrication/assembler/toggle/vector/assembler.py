# src/assembler/toggle/vector/assembler.py

"""
Module: assembler.toggle.vector.assembler
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from fabrication.assembler import ToggleAssembler
from domain.metadata.blueprint.structure.toggle import VectorToggleBlueprint

from artifcat import BuildResult
from domain.structure.toggle import CartesianToggle
from util import LoggingLevelRouter


class VectorToggleAssembler(ToggleAssembler[CartesianToggle]):
    """
    Role
        -   Builder

    Responsibilities:
        1.  Create a VectorToggle instance from the safe blueprint.

    Attributes:

    Provides:
        -   def execute(self, blueprint: VectorToggleBlueprint,) -> BuildResult[VectorToggle]

    Super Class:
        ToggleAssembler
    """
    def __init__(self):
        super().__init__()
    
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: VectorToggleBlueprint,) -> BuildResult[CartesianToggle]:
        """
        Assemble a VectorToggle from the Blueprint's contents.

        Args:
            blueprint: VectorToggleBlueprint
        Returns:
            BuildResult[VectorToggle]
        Raises:
        """
        method = f"{self.__class__.__name__}.execute"
        
        return BuildResult.success(
            VectorToggleBlueprint(coord=blueprint.coord, vector=blueprint.vector)
        )
    
        
        
