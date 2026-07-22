# src/assembler/toggle/vector/assembler.py

"""
Module: assembler.toggle.vector.assembler
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from assembler import ToggleAssembler
from blueprint.toggle import VectorToggleBlueprint

from result import BuildResult
from toggle import VectorToggle
from util import LoggingLevelRouter


class VectorToggleAssembler(ToggleAssembler[VectorToggle]):
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
    def execute(self, blueprint: VectorToggleBlueprint,) -> BuildResult[VectorToggle]:
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
    
        
        
