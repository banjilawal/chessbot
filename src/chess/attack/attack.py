# src/chess/attack/attack.py

"""
Module: chess.attack.attack
Author: Banji Lawal
Created: 2026-01-24
version: 1.0.0
"""

from __future__ import annotations
from typing import cast

from chess.attack import (
    AttackFailedException, AttackResult, AttackerSquareInconsistencyException, AttackerSquareNotFoundException,
    AttackingDisabledEnemyException, AttackingEnemyKingException,
    AttackingFriendlySquareException,
    AttackingTokenOnWrongBoardException, AttackingVacantSquareException
)
from chess.hostage import HostageService
from chess.square import Square, SquareContext, SquareDatabase
from chess.system import LoggingLevelRouter
from chess.system.relation import RelationReport
from chess.team import HostageService
from chess.token import CombatantActivityState, CombatantReadinessEnum, CombatantToken, KingToken, Token, TokenService


class Attack:
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            attacker: Token,
            square: Square,
            token_service: TokenService = TokenService(),
            square_database: SquareDatabase = SquareDatabase(),
            hostage_database_service: HostageService = HostageService(),
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
        square_validation = square_database.integrity_service.validator.validate(candidate=square)
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
        if attacker.team.board != square.occupant.team.board:
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
                    ex=AttackingFriendlySquareException(
                        f"{method}: {AttackingFriendlySquareException.DEFAULT_MESSAGE}"
                    )
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
        if square.occupant.is_disabled:
            # Return the exception chain on failure.
            return AttackResult.failure(
                AttackFailedException(
                    message=f"{method}: {AttackFailedException.DEFAULT_MESSAGE}",
                    ex=AttackingDisabledEnemyException(
                        f"{method}: {AttackingDisabledEnemyException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handoff validating the attacker's square and processing the attack.
        return cls._process_attack(
            attacker=attacker,
            square=square,
            square_database=square_database,
            hostage_database_service=hostage_database_service,
        )
        
        # Set the
    
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _process_attack(
        cls,
        attacker: Token,
        square: Square,
        square_database: SquareDatabase,
        hostage_service: HostageService = HostageService(),
    ) -> AttackResult:
        """"""
        method = "Attack._process_attack"
        
        # Handle the case that removing the captive from their square fails.
        captive_removal = square_database.delete_occupant_by_search(square.occupant)
        if captive_removal.is_failure:
            # Return exception chain on failure.
            return RelationReport.failure(
                AttackFailedException(
                    message=f"{method}: {AttackFailedException.DEFAULT_MESSAGE}",
                    ex=captive_removal.exception
                )
            )
        # Update the hostage's captor field and its status.
        captive = cast(CombatantToken, captive_removal.payload.captor)
        captive.captor = attacker
        captive.activity.classification = CombatantReadinessEnum.CAPTURE_ACTIVATED
        
        # Handle the case that removing the attacker from their old square fails.
        attacker_removal = square_database.delete_occupant_by_search(occupant=attacker)
        if attacker_removal.is_failure:
            # Return exception chain on failure.
            return RelationReport.failure(
                AttackFailedException(
                    message=f"{method}: {AttackFailedException.DEFAULT_MESSAGE}",
                    ex=attacker_removal.exception
                )
            )
        # Handle the case that the transferring the attacker to their conquered square fails.
        add_occupant_result = square_database.add_occupant_to_square(square=square, occupant=attacker)
        if add_occupant_result.is_failure:
            # Return exception chain on failure.
            return RelationReport.failure(
                AttackFailedException(
                    message=f"{method}: {AttackFailedException.DEFAULT_MESSAGE}",
                    ex=attacker_removal.exception
                )
            )
        
        # Build the hostage manifest
        manifest_build_result = hostage_service.builder.build()
        
        # Set the square's captor.
        square.occupant.captor = attacker
        # Update the hostage's activity_status
        square.occupant.activity_state = CombatantActivityState.CAPTURE_ACTIVATED
        # Remove the enemy from their square.
        hostage = square.occupant
        # Set the square's new occupant.
        square.occupant = attacker
        
        # Remove the attacker from their old square
        
    @classmethod
    @LoggingLevelRouter.monitor
    def _attacker_leaves_square(attacker: Token, attack_square: Square) -> Deletion
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _process_attacker_square(
            cls,
            attacker: Token,
            square_database: SquareDatabase,
    ) -> RelationReport[Square, Token]:
        method = "Attack._process_attacker_square"
        
        # --- Search for the attacker's square from their board. ---#
        square_search = attacker.team.board.squares.search_squares(
            context=SquareContext(coord=attacker.current_position)
        )
        # Handle the case that the square_search fails.
        if square_search.is_failure:
            # Return exception chain on failure.
            return RelationReport.failure(
                AttackFailedException(
                    message=f"{method}: {AttackFailedException.DEFAULT_MESSAGE}",
                    ex=AttackingEnemyKingException(
                        f"{method}: {AttackingEnemyKingException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that no square matching the occupant's coords is found.
        if square_search.is_empty:
            # Return exception chain on failure.
            return RelationReport.failure(
                AttackFailedException(
                    message=f"{method}: {AttackFailedException.DEFAULT_MESSAGE}",
                    ex=AttackerSquareNotFoundException(
                        f"{method}: {AttackerSquareNotFoundException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # If there is more than one square in the result at least one of them is stale.
        if len(set(square_search)) > 1:
            # Return exception chain on failure.
            return RelationReport.failure(
                AttackFailedException(
                    message=f"{method}: {AttackFailedException.DEFAULT_MESSAGE}",
                    ex=ConflictingAttackerSquareException(
                        f"{method}: {ConflictingAttackerSquareException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # --- Run the relationship analysis between the attacker and their square. ---#
        
    
        square = cast(Square, square_search.payload[0])
        
        relation_analysis = square_service.square_token_relation_analyzer.analyze(
            candidate_primary=square,
            candidate_satellite=attacker
        )
        # Handle the case that the analysis is not completed.
        if relation_analysis.is_failure:
            # Return exception chain on failure.
            return RelationReport.failure(
                AttackFailedException(
                    message=f"{method}: {AttackFailedException.DEFAULT_MESSAGE}",
                    ex=relation_analysis.exception
                )
            )
        # Handle the case that there is no bidirectional_relation
        if  not relation_analysis.fully_exists:
            # Return exception chain on failure.
            return RelationReport.failure(
                AttackFailedException(
                    message=f"{method}: {AttackFailedException.DEFAULT_MESSAGE}",
                    ex=AttackerSquareInconsistencyException(
                        f"{method}: {AttackerSquareInconsistencyException.DEFAULT_MESSAGE}"
                    )
                )
            )
        return relation_analysis
        
            