# src/assembler/model/token/assembler.py

"""
Module: assembler.model.token.assembler
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from assembler import ModelAssembler
from blueprint import TokenBlueprint
from result import BuildResult

from util import LoggingLevelRouter
from model import CombatantToken, King, KingToken, Pawn, PawnToken, Token

class TokenAssembler(ModelAssembler[Token]):
    """
    Role
        -   Builder

    Responsibilities:
        1.  Create a Token instance from the safe blueprint.

    Attributes:

    Provides:
        -   def execute(self, blueprint: TokenBlueprint,) -> BuildResult[Token]

    Super Class:
        ModelAssembler
    """
    
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: TokenBlueprint,) -> BuildResult[Token]:
        """
        Assemble a Token from the Blueprint's contents.

        Args:
            blueprint: TokenBlueprint
        Returns:
            BuildResult[Token]
        Raises:
        """
        method = f"{self.__class__.__name__}.execute"
        
        if isinstance(blueprint.rank, Pawn):
            return BuildResult.success(
                PawnToken(
                    id=blueprint.id,
                    team=blueprint.team,
                    formation=blueprint.formation,
                    home_square=blueprint.home_square,
                )
            )
        if isinstance(blueprint.rank, King):
            return BuildResult.success(
                KingToken(
                    id=blueprint.id,
                    team=blueprint.team,
                    formation=blueprint.formation,
                    home_square=blueprint.home_square
                )
            )
        return BuildResult.success(
            CombatantToken(
                id=blueprint.id,
                team=blueprint.team,
                formation=blueprint.formation,
                home_square=blueprint.home_square,
                rank=blueprint.rank
            )
        )