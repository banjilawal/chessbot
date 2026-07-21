# src/assembler/model/coord/py

"""
Module: assembler.model.coord.assembler
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from blueprint import CoordBlueprint
from result import BuildResult
from assembler import ModelAssembler
from util import LoggingLevelRouter
from model import Coord
from controller import WorkerRegistryController

class CoordAssembler(ModelAssembler[Coord]):
    """
    Role
        -   Build Process Owner

    Responsibilities:
        1.  Create a Coord instance from the safe blueprint.

    Attributes:

    Provides:
        -   def execute(self, blueprint: CoordBlueprint,) -> BuildResult[Coord]

    Super Class:
        ModelAssembler
    """

    @LoggingLevelRouter.monitor
    def execute(self, blueprint: CoordBlueprint,) -> BuildResult[Coord]:
        """
        Assemble a Coord from the Blueprint's contents.

        Args:
            blueprint: CoordBlueprint
        Returns:
            BuildResult[Coord]
        Raises:
        """
        method = f"{self.__class__.__name__}.execute"
        return BuildResult.success(
            Coord(row=blueprint.row, column=blueprint.column,)
        )
        
        
