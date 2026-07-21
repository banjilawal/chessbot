# src/assembler/model/rank/py

"""
Module: assembler.model.rank.assembler
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from blueprint import RankBlueprint
from model import Bishop, King, Knight, Pawn, Queen, Rank, Rook
from result import BuildResult
from assembler import ModelAssembler
from schema import Persona
from util import LoggingLevelRouter


class RankAssembler(ModelAssembler[Rank]):
    """
    Role
        -   Build Process Owner

    Responsibilities:
        1.  Create a Rank instance from the safe blueprint.

    Attributes:

    Provides:
        -   def execute(self, blueprint: RankBlueprint,) -> BuildResult[Rank]

    Super Class:
        ModelAssembler
    """
    
    
    @LoggingLevelRouter.monitor()
    def execute(self, blueprint: RankBlueprint,) -> BuildResult[Rank]:
        """
        Assemble a Rank from the Blueprint's contents.

        Args:
            blueprint: RankBlueprint
        Returns:
            BuildResult[Rank]
        Raises:
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Route to the appropriate concrete integrity.build. ---#
        
        # Entry point into building a King instance.
        if blueprint.persona == Persona.KING:
            return BuildResult.success(
                King(persona=blueprint.persona)
            )
        # Entry point into building a Pawn instance.
        if blueprint.persona == Persona.PAWN:
            return BuildResult.success(
                Pawn(persona=blueprint.persona)
            )
        # Entry point into building a Knight instance.
        if blueprint.persona == Persona.KNIGHT:
            return BuildResult.success(
                Knight(persona=blueprint.persona)
            )
        # Entry point into building a Bishop instance.
        if blueprint.persona == Persona.BISHOP:
            return BuildResult.success(
                Bishop(persona=blueprint.persona)
            )
        # Entry point into building a Rook instance.
        if blueprint.persona == Persona.ROOK:
            return BuildResult.success(
                Rook(persona=blueprint.persona)
            )
        # Entry point into building a Queen instance.
        if blueprint.persona == Persona.QUEEN:
            return BuildResult.success(
                Queen(persona=blueprint.persona)
            )
        