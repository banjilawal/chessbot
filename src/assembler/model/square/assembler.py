# src/assembler/model/square/assembler.py

"""
Module: assembler.model.square.assembler
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from blueprint import SquareBlueprint
from model import HomeSquare, Square
from result import BuildResult
from assembler import ModelAssembler
from util import LoggingLevelRouter


class SquareAssembler(ModelAssembler[Square]):
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