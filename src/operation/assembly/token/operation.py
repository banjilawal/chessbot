# src/operation/assembly/token/operation.py

"""
Module: operation.assembly.token.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from blueprint import TokenBlueprint
from result import BuildResult
from operation import Assembler
from util import LoggingLevelRouter
from controller import WorkerRegistryController
from model import CombatantToken, King, KingToken, Pawn, PawnToken, Token

class TokenAssembler(Assembler[Token]):
    NAME = "token_assembler"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(cls, blueprint: TokenBlueprint,) -> BuildResult[Token]:
        """
        Assemble the appropriate Token.

        Args:
            blueprint: TokenBlueprint
        Returns:
            BuildResult[Token]
        Raises:
        """
        method = f"{cls.__name__}.execute"
        
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

# Register the operation.
WorkerRegistryController.register_worker(TokenAssembler)