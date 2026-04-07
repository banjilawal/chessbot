# src/integrity/build/token/builder.py

"""
Module: integrity.build.token.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from model import CombatantToken, King, KingToken, Pawn, PawnToken, Token, TokenBlueprint
from operation import Creator
from result import BuildResult
from system import  LoggingLevelRouter


class TokenCreator(Creator[Token]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(cls, blueprint: TokenBlueprint,) -> BuildResult[Token]:
        method = f"{cls.__name__}.execute"
        
        
        if isinstance(blueprint.rank, Pawn):
            return BuildResult.success(
                PawnToken(
                    id=blueprint.id,
                    team=blueprint.team,
                    designation=blueprint.formation.designation,
                    roster_number=blueprint.formation.roster_number,
                    opening_square_name=blueprint.formation.square_name
                )
            )
        if isinstance(blueprint.rank, King):
            return BuildResult.success(
                KingToken(
                    id=blueprint.id,
                    team=blueprint.team,
                    designation=blueprint.formation.designation,
                    roster_number=blueprint.formation.roster_number,
                    opening_square_name=blueprint.formation.square_name
                )
            )
        return BuildResult.success(
            CombatantToken(
                id=blueprint.id,
                team=blueprint.team,
                designation=blueprint.formation.designation,
                roster_number=blueprint.formation.roster_number,
                opening_square_name=blueprint.formation.square_name,
                rank=blueprint.rank
            )
        )
