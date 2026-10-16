# src/fabrication/builder/model/rank/fabrication/builder.py

"""
Module: fabrication.builder.model.rank.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from domain.metadata.blueprint import RankBlueprint
from domain.model import Bishop, King, Knight, Pawn, Queen, Rank, Rook
from artifcat import BuildResult
from fabrication.builder import ModelBuilder
from domain.schema import Persona
from util import LoggingLevelRouter


class RankBuilder(ModelBuilder[Rank]):
    """
    Role
        - Builder

    Responsibilities:
        1.  Create a Rank instance from the safe blueprint.

    Attributes:

    Provides:
        -   def execute(self, blueprint: RankBlueprint,) -> BuildResult[Rank]

    Super Class:
        ModelBuilder
    """
    
    
    @LoggingLevelRouter.monitor()
    def execute(self, request: RankBlueprint, ) -> BuildResult[Rank]:
        """
        Assemble a Rank from the Blueprint's contents.

        Args:
            request: RankBlueprint
        Returns:
            BuildResult[Rank]
        Raises:
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Route to the appropriate concrete integrity.build. ---#
        
        # Entry point into building a King instance.
        if request.persona == Persona.KING:
            return BuildResult.success(
                King(persona=request.persona)
            )
        # Entry point into building a Pawn instance.
        if request.persona == Persona.PAWN:
            return BuildResult.success(
                Pawn(persona=request.persona)
            )
        # Entry point into building a Knight instance.
        if request.persona == Persona.KNIGHT:
            return BuildResult.success(
                Knight(persona=request.persona)
            )
        # Entry point into building a Bishop instance.
        if request.persona == Persona.BISHOP:
            return BuildResult.success(
                Bishop(persona=request.persona)
            )
        # Entry point into building a Rook instance.
        if request.persona == Persona.ROOK:
            return BuildResult.success(
                Rook(persona=request.persona)
            )
        # Entry point into building a Queen instance.
        if request.persona == Persona.QUEEN:
            return BuildResult.success(
                Queen(persona=request.persona)
            )
        