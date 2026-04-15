# src/integrity/assemble/token/assembler.py

"""
Module: integrity.assemble.token.assembler
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from operation import Assembler
from result import BuildResult
from system import  LoggingLevelRouter
from model import CombatantToken, King, KingToken, Pawn, PawnToken, Token, TokenBlueprint

class TokenAssembler(Assembler[Token]):
    
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
                    designation=blueprint.formation.designation,
                    roster_number=blueprint.formation.roster_number,
                    opening_square=blueprint.opening_square,
                )
            )
        if isinstance(blueprint.rank, King):
            return BuildResult.success(
                KingToken(
                    id=blueprint.id,
                    team=blueprint.team,
                    designation=blueprint.formation.designation,
                    roster_number=blueprint.formation.roster_number,
                    opening_square=blueprint.opening_square
                )
            )
        return BuildResult.success(
            CombatantToken(
                id=blueprint.id,
                team=blueprint.team,
                designation=blueprint.formation.designation,
                roster_number=blueprint.formation.roster_number,
                opening_square=blueprint.opening_square,
                rank=blueprint.rank
            )
        )
