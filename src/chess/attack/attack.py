# src/chess/attack/attack.py

"""
Module: chess.attack.attack
Author: Banji Lawal
Created: 2026-01-24
version: 1.0.0
"""
from chess.attack import AttackResult
from chess.square import Square, SquareService
from chess.system import LoggingLevelRouter
from chess.token import Token, TokenService


class Attack:
    
    @classmethod
    @LoggingLevelRouter
    def execute(
            cls,
            attacker: Token,
            square: Square,
            token_service: TokenService = TokenService(),
            square_service: SquareService = SquareService(),
    ) -> AttackResult:
        method = "Attack.execute"
        attacker_validation = token_service.verify_actionable_token(attacker)
        if attacker_validation.is_failure:
            return AttackResult.failure(
                AttackFailedException(
                    message=f"{method}: {AttackFailedException.DEFAULT_MESSAGE}",
                    ex=attacker_validation.exception
                )
            )
        square_validation = square_service.validator.validate(candidate=square)
        if square_validation.is_failure:
            return AttackResult.failure(
                AttackFailedException(
                    message=f"{method}: {AttackFailedException.DEFAULT_MESSAGE}",
                    ex=square_validation.exception
                )
            )
        
        return AttackResult.success()
        