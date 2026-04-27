# src/operation/assembly/square/operation.py

"""
Module: operation.assembly.square.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from result import BuildResult
from operation import Assembler
from system import LoggingLevelRouter
from model import OpeningSquare, Square, SquareBlueprint


class SquareAssembler(Assembler[Square]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Build Process Owner

    Responsibilities:
        1.  Ensure a new Square instance is born safe and reliable.

    Attributes:

    Provides:
        -   def execute(
                    owner: Square,
                    id: int = IdFactory,
                    formation: Formation,
                    rank_service: RankService,
                    identity_service: IdentityService,
                    formation_service: FormationService,
                    square_validator: SquareValidator,
            ) -> BuildResult[Square]

     Super Class:
        .Assembly.
     """
    OPERATION_NAME = "square_assembler"
    
    @classmethod
    @LoggingLevelRouter.monitor()
    def execute(cls, blueprint: SquareBlueprint,) -> BuildResult[Square]:
        """
        Action:
            1.  Send an exception chain in the BuildResult if
                    -   Any build param fails does not pass a validation check.
                    -   The square's attributes have already been used on the board.
            2.  Build the Square instance with the params.
            3.  Send an exception chain in the BuildResult if
                    * The square requires insertion into the board but the insertion fails.
            4.  Return the Square instance in the BuildResult.
        Args:
            blueprint: SquareBlueprint
        Returns:
            BuildResult[Square]
            
        Raises:
        """
        method = f"{cls.__class__.__name__}.build"
        
        if blueprint.formation is not None:
            return BuildResult.success(
                OpeningSquare(
                    id=blueprint.id,
                    name=blueprint.name,
                    coord=blueprint.coord,
                    board=blueprint.board,
                    formation=blueprint.formation,
                )
            )
        return BuildResult.success(
            Square(
                id=blueprint.id,
                name=blueprint.name,
                coord=blueprint.coord,
                board=blueprint.board,
            )
        )