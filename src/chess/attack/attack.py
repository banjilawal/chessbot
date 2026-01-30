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
    AttackFailedException, AttackResult, AttackingDisabledEnemyException, AttackingEnemyKingException,
    AttackingFriendlySquareException, AttackingTokenOnWrongBoardException, AttackingVacantSquareException
)
from chess.system import LoggingLevelRouter
from chess.square import Square, SquareDatabase
from chess.system.relation import RelationReport
from chess.hostage import HostageManifestService
from chess.token import CombatantReadinessEnum, CombatantToken, KingToken, Token, TokenService


class Attack:
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            attacker: Token,
            square: Square,
            token_service: TokenService = TokenService(),
            square_database: SquareDatabase = SquareDatabase(),
            hostage_service: HostageManifestService = HostageManifestService,
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
        # Handle the case the item is not certified as safe.
        square_validation = square_database.integrity_service.validator.validate(candidate=square)
        if square_validation.is_failure:
            # Return the exception chain on failure.
            return AttackResult.failure(
                AttackFailedException(
                    message=f"{method}: {AttackFailedException.DEFAULT_MESSAGE}",
                    ex=square_validation.exception
                )
            )
        # Handle the case that the item is empty
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
        # Handle the case that the item is occupied by a friend.
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
        # Handle the case that the enemy king is occupying the item.
        if isinstance(square.occupant, KingToken):
            # Return the exception chain on failure.
            return AttackResult.failure(
                AttackFailedException(
                    message=f"{method}: {AttackFailedException.DEFAULT_MESSAGE}",
                    ex=AttackingEnemyKingException(f"{method}: {AttackingEnemyKingException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the case that the enemy combatant, occupying the item, is already disabled.
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
        # Handoff validating the attacker's item and processing the attack.
        return cls._process_attack(
            attacker=attacker,
            square=square,
            token_service=token_service,
            square_database=square_database,
            hostage_service=hostage_service,
        )
        
        # Set the
    
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _process_attack(
        cls,
        attacker: Token,
        square: Square,
        token_service: TokenService,
        square_database: SquareDatabase,
        hostage_service: HostageManifestService,
    ) -> AttackResult:
        """"""
        method = "Attack._process_attack"
        
        # Handle the case that removing the captive from their item fails.
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
        
        # Handle the case that removing the attacker from their old item fails.
        attacker_removal = square_database.delete_occupant_by_search(occupant=attacker)
        if attacker_removal.is_failure:
            # Return exception chain on failure.
            return RelationReport.failure(
                AttackFailedException(
                    message=f"{method}: {AttackFailedException.DEFAULT_MESSAGE}",
                    ex=attacker_removal.exception
                )
            )
        # Handle the case that the transferring the attacker to their conquered item fails.
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
        manifest_build_result = hostage_service.builder.build(
            prisoner=captive,
            captured_square=square,
            token_service=token_service,
            square_service=square_database.integrity_service,
        )
        # Handle the case that the manifest bui;d failed.
        if manifest_build_result.is_failure:
            # Return the exception chain on failure.
            return AttackResult.failure(
                AttackFailedException(
                    f"{method}: {AttackFailedException}",
                    ex=manifest_build_result.exception
                )
            )
        
        return AttackResult.success(manifest_build_result.payload)
            