# src/assembly/coord/py

"""
Module: assembly.coord.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from blueprint import CoordBlueprint
from result import BuildResult
from operation import Assembler
from util import LoggingLevelRouter
from model import Coord
from controller import WorkerRegistryController

class CoordAssembler(Assembler[Coord]):
    NAME = "coord_assembler"
    
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

# Register the 
WorkerRegistryController.register_worker(worker=CoordAssembler)
        
        
