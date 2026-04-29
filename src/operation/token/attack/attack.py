# src/logic/attack/attack.py

"""
Module: logic.attack.attack
Author: Banji Lawal
Created: 2026-01-24
version: 1.0.0
"""

from __future__ import annotations

from operation.token.attack import (
    AttackException, AttackResult, AttackingDisabledEnemyException, AttackingEnemyKingException,
    AttackingFriendlySquareException, AttackingTokenOnWrongBoardException, AttackingVacantSquareException
)
from util import LoggingLevelRouter
from logic.square import Square, SquareDatabase
from system import RelationReport
from model.hostage import HostageService
from model.token import CombatantReadinessEnum, KingToken, Token, TokenBoardState, TokenService


class Attack:
    OPERATION_NAME = "arena_validator"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            attacker: Token,
            square: Square,
            token_service: TokenService = TokenService(),
            square_database: SquareDatabase = SquareDatabase(),
            hostage_service: HostageService = HostageService,
    ) -> AttackResult:
        method = "Attack.execute"
        
        # Handle the case that, the attacker is disabled
        attacker_validation = token_service.verify_actionable_token(token=attacker)
        if attacker_validation.is_failure:
            # Return exception chain on failure.
            return AttackResult.failure(
                AttackException(
                    msg=f"{method}: {AttackException.MSG}",
                    ex=attacker_validation.exception
                )
            )
        # Handle the case the item does not pass a validation check.
        square_validation = square_database.microservice.validator.validate(candidate=square)
        if square_validation.is_failure:
            # Send the exception chain on failure.
            return AttackResult.failure(
                AttackException(
                    msg=f"{method}: {AttackException.MSG}",
                    ex=square_validation.exception
                )
            )
        # Handle the case that, the item is empty
        if square.is_empty:
            # Send the exception chain on failure.
            return AttackResult.failure(
                AttackException(
                    msg=f"{method}: {AttackException.MSG}",
                    ex=AttackingVacantSquareException(f"{method}: {AttackingVacantSquareException.MSG}")
                )
            )
        # Handle the case that, the tokens are on different boards.
        if attacker.team.board != square.occupant.team.board:
            # Send the exception chain on failure.
            return AttackResult.failure(
                AttackException(
                    msg=f"{method}: {AttackException.MSG}",
                    ex=AttackingTokenOnWrongBoardException(
                        f"{method}: {AttackingTokenOnWrongBoardException.MSG}"
                    )
                )
            )
        # Handle the case that, the item is occupied by a friend.
        if not attacker.is_enemy(square.occupant):
            # Send the exception chain on failure.
            return AttackResult.failure(
                AttackException(
                    msg=f"{method}: {AttackException.MSG}",
                    ex=AttackingFriendlySquareException(
                        f"{method}: {AttackingFriendlySquareException.MSG}"
                    )
                )
            )
        # Handle the case that, the enemy king is occupying the item.
        if isinstance(square.occupant, KingToken):
            # Send the exception chain on failure.
            return AttackResult.failure(
                AttackException(
                    msg=f"{method}: {AttackException.MSG}",
                    ex=AttackingEnemyKingException(f"{method}: {AttackingEnemyKingException.MSG}")
                )
            )
        # Handle the case that, the enemy combatant, occupying the item, is already disabled.
        if square.occupant.is_disabled:
            # Send the exception chain on failure.
            return AttackResult.failure(
                AttackException(
                    msg=f"{method}: {AttackException.MSG}",
                    ex=AttackingDisabledEnemyException(
                        f"{method}: {AttackingDisabledEnemyException.MSG}"
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
        hostage_service: HostageService,
    ) -> AttackResult:
        """"""
        method = "Attack._process_attack"
        
        # Handle the case that, removing the captive from their item fails.
        captive_removal = square_database.delete_occupant_by_search(square.occupant)
        if captive_removal.is_failure:
            # Return exception chain on failure.
            return RelationReport.failure(
                AttackException(
                    msg=f"{method}: {AttackException.MSG}",
                    ex=captive_removal.exception
                )
            )
        # Update the hostage's captor field and its status.
        prisoner = captive_removal.payload
        prisoner.captor = attacker
        prisoner.board_state = TokenBoardState.REMOVED_FROM_BOARD
        prisoner.activity.classification = CombatantReadinessEnum.CAPTURE_ACTIVATED
        
        # Handle the case that, removing the attacker from their old item fails.
        attacker_removal = square_database.delete_occupant_by_search(occupant=attacker)
        if attacker_removal.is_failure:
            # Return exception chain on failure.
            return RelationReport.failure(
                AttackException(
                    msg=f"{method}: {AttackException.MSG}",
                    ex=attacker_removal.exception
                )
            )
        # Handle the case that, the transferring the attacker to their conquered item fails.
        add_occupant_result = square_database.add_occupant_to_square(square=square, occupant=attacker)
        if add_occupant_result.is_failure:
            # Return exception chain on failure.
            return RelationReport.failure(
                AttackException(
                    msg=f"{method}: {AttackException.MSG}",
                    ex=attacker_removal.exception
                )
            )
        
        # Build the hostage manifest
        manifest_build_result = hostage_service.builder.build(
            prisoner=prisoner,
            captured_square=square,
            token_service=token_service,
            square_service=square_database.microservice,
        )
        # Handle the case that, the manifest bui;d failed.
        if manifest_build_result.is_failure:
            # Send the exception chain on failure.
            return AttackResult.failure(
                AttackException(
                    f"{method}: {AttackException}",
                    ex=manifest_build_result.exception
                )
            )
        
        return AttackResult.success(manifest_build_result.payload)
            