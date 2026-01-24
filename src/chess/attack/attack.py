# src/chess/attack/attack.py

"""
Module: chess.attack.attack
Author: Banji Lawal
Created: 2026-01-24
version: 1.0.0
"""
from typing import cast

from chess.attack import (
    AttackFailedException, AttackResult, AttackerSquareInconsistencyException, AttackingEnemyKingException,
    AttackingFriendlySquareException,
    AttackingTokenOnWrongBoardException, AttackingVacantSquareException
)
from chess.hostage import HostageDatabaseService, HostageDatabaseService
from chess.square import Square, SquareContext, SquareService
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
            hostage_database_service: HostageDatabaseService = HostageDatabaseService(),
    ) -> AttackResult:
        method = "Attack.execute"
        
        # Handle the case that the attacker is disabled
        attacker_validation = token_service.verify_actionable_token(token=attacker)
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
        # Handle the case that the tokens are on different boards.
        if attacker.team.board != square.occupant.team.boardy:
            # Return the exception chain on failure.
            return AttackResult.failure(
                AttackFailedException(
                    message=f"{method}: {AttackFailedException.DEFAULT_MESSAGE}",
                    ex=AttackingTokenOnWrongBoardException(
                        f"{method}: {AttackingTokenOnWrongBoardException.DEFAULT_MESSAGE}"
                    )
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
        if isinstance(square.occupant, KingToken):
            # Return the exception chain on failure.
            return AttackResult.failure(
                AttackFailedException(
                    message=f"{method}: {AttackFailedException.DEFAULT_MESSAGE}",
                    ex=AttackingEnemyKingException(f"{method}: {AttackingEnemyKingException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the case that the enemy combatant, occupying the square, is already disabled.
        if isinstance(square.occupant, KingToken):
            # Return the exception chain on failure.
            return AttackResult.failure(
                AttackFailedException(
                    message=f"{method}: {AttackFailedException.DEFAULT_MESSAGE}",
                    ex=AttackingEnemyKingException(f"{method}: {AttackingEnemyKingException.DEFAULT_MESSAGE}")
                )
            )
        # Handoff validating the attacker's square and processing the attack.
        return cls._process_attack(
            attacker=attacker,
            square=square,
            hostage_database_service=hostage_database_service
        )
        
        # Set the
    
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _process_attack(
        cls,
        attacker: Token,
        square: Square,
        hostage_database_service: HostageDatabaseService,
    ) -> AttackResult:
        """"""
        method = "Attack._process_attack"
        square_search_result = attacker.team.board.squares.search_squares(
            context=SquareContext(coord=attacker.current_position)
        )
        # Handle the case that the square_search fails.
        if square_search_result.is_failure:
            # Return exception chain on failure.
            return AttackResult.failure(
                AttackFailedException(
                    message=f"{method}: {AttackFailedException.DEFAULT_MESSAGE}",
                    ex=AttackingEnemyKingException(f"{method}: {AttackingEnemyKingException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the case that no square matching the token's coords is found.
        if square_search_result.is_empty:
            # Return exception chain on failure.
            return AttackResult.failure(
                AttackFailedException(
                    message=f"{method}: {AttackFailedException.DEFAULT_MESSAGE}",
                    ex=AttackingEnemyKingException(f"{method}: {AttackingEnemyKingException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the case that the square does not contain the attacker despite their share coord.
        if cast(Square, square_search_result.payload).occupant != attacker:
            # Return exception chain on failure.
            return AttackResult.failure(
                AttackFailedException(
                    message=f"{method}: {AttackFailedException.DEFAULT_MESSAGE}",
                    ex=AttackerSquareInconsistencyException(
                        f"{method}: {AttackerSquareInconsistencyException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # --- Start Processing the attack. ---#