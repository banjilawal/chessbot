# src/operation/assemble/coord/operation.py

"""
Module: operation.assemble.coord.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from operation import Assembler
from result import BuildResult
from system import  LoggingLevelRouter
from model import Board, Coord, CoordBlueprint

class CoordAssembler(Assembler[Coord]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(cls, blueprint: CoordBlueprint,) -> BuildResult[Coord]:
        """
        Assemble the appropriate Coord.

        Args:
            blueprint: CoordBlueprint
        Returns:
            BuildResult[Coord]
        Raises:
        """
        method = f"{cls.__name__}.execute"
        return BuildResult.success(
            Coord(
                row=blueprint.row,
                column=blueprint.column,
            )
        )
        
        
