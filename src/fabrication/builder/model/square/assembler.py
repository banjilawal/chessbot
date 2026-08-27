# src/fabrication/builder/model/square/fabrication/builder.py

"""
Module: fabrication.builder.model.square.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain.metadata.blueprint import SquareBlueprint
from domain.model import HomeSquare, Square
from artifcat import BuildResult
from fabrication.builder import ModelBuilder
from util import LoggingLevelRouter


class SquareBuilder(ModelBuilder[Square]):
    """
    Role
        -  Builder

    Responsibilities:
        1.  Create a Vector instance from the safe blueprint.

    Attributes:

    Provides:
        - def execute(self, blueprint: VectorBlueprint,) -> BuildResult[Vector]

    Super Class:
        ModelBuilder
    """
    

    @LoggingLevelRouter.monitor()
    def execute(self, blueprint: SquareBlueprint,) -> BuildResult[Square]:
        """
        Action:
            1.  Assemble the square from the Blueprint.
        Args:
            blueprint: SquareBlueprint
        Returns:
            BuildResult[Square]
        Raises:
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the blueprint is for a HomeSquare.
        if blueprint.formation is not None:
            return BuildResult.success(
                HomeSquare(
                    id=blueprint.id,
                    name=blueprint.name,
                    coord=blueprint.coord,
                    board=blueprint.board,
                    formation=blueprint.formation,
                )
            )
        # For the alternative return a plain old Square,
        return BuildResult.success(
            Square(
                id=blueprint.id,
                name=blueprint.name,
                coord=blueprint.coord,
                board=blueprint.board,
            )
        )