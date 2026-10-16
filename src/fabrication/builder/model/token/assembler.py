# src/fabrication/builder/model/token/fabrication/builder.py

"""
Module: fabrication.builder.model.token.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from fabrication.builder import ModelBuilder
from domain.metadata.blueprint import TokenBlueprint
from artifcat import BuildResult

from util import LoggingLevelRouter
from domain.model import CombatantToken, King, KingToken, Pawn, PawnToken, Token

class TokenBuilder(ModelBuilder[Token]):
    """
    Role
        - Builder

    Responsibilities:
        1.  Create a Token instance from the safe blueprint.

    Attributes:

    Provides:
        -   def execute(self, blueprint: TokenBlueprint,) -> BuildResult[Token]

    Super Class:
        ModelBuilder
    """
    
    
    @LoggingLevelRouter.monitor
    def execute(self, request: TokenBlueprint, ) -> BuildResult[Token]:
        """
        Assemble a Token from the Blueprint's contents.

        Args:
            request: TokenBlueprint
        Returns:
            BuildResult[Token]
        Raises:
        """
        method = f"{self.__class__.__name__}.execute"
        
        if isinstance(request.rank, Pawn):
            return BuildResult.success(
                PawnToken(
                    id=request.id,
                    team=request.team,
                    formation=request.formation,
                    home_square=request.home_square,
                )
            )
        if isinstance(request.rank, King):
            return BuildResult.success(
                KingToken(
                    id=request.id,
                    team=request.team,
                    formation=request.formation,
                    home_square=request.home_square
                )
            )
        return BuildResult.success(
            CombatantToken(
                id=request.id,
                team=request.team,
                formation=request.formation,
                home_square=request.home_square,
                rank=request.rank
            )
        )