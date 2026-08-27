# src/fabrication/builder/model/coord/fabrication/builder.py

"""
Module: fabrication.builder.model.coord.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain.metadata.blueprint import CoordBlueprint
from artifcat import BuildResult
from fabrication.builder import ModelBuilder
from util import LoggingLevelRouter
from domain.model import Coord

class CoordBuilder(ModelBuilder[Coord]):
    """
    Role
        -  Builder

    Responsibilities:
        1.  Create a Coord instance from the safe blueprint.

    Attributes:

    Provides:
        - def execute(self, blueprint: CoordBlueprint,) -> BuildResult[Coord]

    Super Class:
        ModelBuilder
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
        
        
