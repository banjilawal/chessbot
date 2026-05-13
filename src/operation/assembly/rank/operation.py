# src/operation/assembly/rank/operation.py

"""
Module: operation.assembly.rank.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from result import BuildResult
from operation import Assembler
from util import LoggingLevelRouter
from controller import WorkerRegistryController
from model import Bishop, King, Knight, Pawn, Persona, Queen, Rank, RankBlueprint, Rook



class RankAssembler(Assembler[Rank]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Build Process Owner

    Responsibilities:
        1.  Ensure a new Rank instance is born safe and reliable.

    Attributes:

    Provides:
        -   def execute(blueprint: RankBlueprint) -> BuildResult[Rank]:

     Super Class:
        Assembler
     """
    NAME = "rank_assembler"
    
    @classmethod
    @LoggingLevelRouter.monitor()
    def execute(cls, blueprint: RankBlueprint,) -> BuildResult[Rank]:
        """
        Action:
            1.  Send an exception chain in the BuildResult if
                    -   Any build param fails does not pass a validation check.
                    -   The rank's attributes have already been used on the board.
            2.  Build the Rank instance with the params.
            3.  Send an exception chain in the BuildResult if
                    * The rank requires insertion into the board but the insertion fails.
            4.  Return the Rank instance in the BuildResult.
        Args:
            blueprint: RankBlueprint
        Returns:
            BuildResult[Rank]
            
        Raises:
        """
        method = f"{cls.__class__.__name__}.build"
        
        # --- Route to the appropriate concrete integrity.build. ---#
        
        # Entry point into building a King instance.
        if blueprint.persona == Persona.KING:
            return BuildResult.success(King(id=blueprint.id, persona=blueprint.persona))
        # Entry point into building a Pawn instance.
        if blueprint.persona == Persona.PAWN:
            return BuildResult.success(Pawn(id=blueprint.id, persona=blueprint.persona))
        # Entry point into building a Knight instance.
        if blueprint.persona == Persona.KNIGHT:
            return BuildResult.success(Knight(id=blueprint.id, persona=blueprint.persona))
        # Entry point into building a Bishop instance.
        if blueprint.persona == Persona.BISHOP:
            return BuildResult.success(Bishop(id=blueprint.id, persona=blueprint.persona))
        # Entry point into building a Rook instance.
        if blueprint.persona == Persona.ROOK:
            return BuildResult.success(Rook(id=blueprint.id, persona=blueprint.persona))
        # Entry point into building a Queen instance.
        if blueprint.persona == Persona.QUEEN:
            return BuildResult.success(Queen(id=blueprint.id, persona=blueprint.persona))

# Register the operation.
WorkerRegistryController.register(worker=RankAssembler)
        