# src/operation/assembly/coord/operation.py

"""
Module: operation.assembly.coord.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from result import BuildResult
from operation import Assembler
from system import LoggingLevelRouter
from model import Coord, CoordBlueprint

class CoordAssembler(Assembler[Coord]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(cls, blueprint: CoordBlueprint,) -> BuildResult[Coord]:
        """
       .Assembly.he appropriate Coord.

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
        
        
