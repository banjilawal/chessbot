# src/chess/attack/attack.py

"""
Module: chess.attack.attack
Author: Banji Lawal
Created: 2026-01-24
version: 1.0.0
"""
from chess.attack import (
    AttackFailedException, AttackResult, AttackingEnemyKingException, AttackingFriendlySquareException,
    AttackingVacantSquareException
)
from chess.square import Square, SquareService
from chess.system import LoggingLevelRouter
from chess.token import KingToken, Token, TokenService


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
        
        # Handle the case that the attacker is disabled
        attacker_validation = token_service.verify_actionable_token(candidate=attacker)
        if attacker_validation.is_failure:
            # Return exception chain on failure.
            return AttackResult.failure(
                AttackFailedException(
                    message=f"{method}: {AttackFailedException.DEFAULT_MESSAGE}",
                    ex=attacker_validation.exception
                )
            )
        # Handle the case the square is not certified as safe.
        square_validation = square_service.validator.validate(candidate=square)
        if square_validation.is_failure:
            # Return the exception chain on failure.
            return AttackResult.failure(
                AttackFailedException(
                    message=f"{method}: {AttackFailedException.DEFAULT_MESSAGE}",
                    ex=square_validation.exception
                )
            )
        # Handle the case that the square is empty
        if square.is_empty:
            # Return the exception chain on failure.
            return AttackResult.failure(
                AttackFailedException(
                    message=f"{method}: {AttackFailedException.DEFAULT_MESSAGE}",
                    ex=AttackingVacantSquareException(f"{method}: {AttackingVacantSquareException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the case that the square is occupied by a friend.
        if not attacker.is_enemy(square.occupant):
            # Return the exception chain on failure.
            return AttackResult.failure(
                AttackFailedException(
                    message=f"{method}: {AttackFailedException.DEFAULT_MESSAGE}",
                    ex=AttackingFriendlySquareException(f"{method}: {AttackingFriendlySquareException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the case that the enemy king is occupying the square.
        if isinstance(KingToken, square.occupant):
            # Return the exception chain on failure.
            return AttackResult.failure(
                AttackFailedException(
                    message=f"{method}: {AttackFailedException.DEFAULT_MESSAGE}",
                    ex=AttackingEnemyKingException(f"{method}: {AttackingEnemyKingException.DEFAULT_MESSAGE}")
                )
            )
        
        return AttackResult.success()
        