# src/chess/piece/travel/attack/validator.py

"""
Module: `chess.piece.travel.attack.validator`
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import Any, Tuple, cast

from chess.board import Board, BoardPieceSearch, BoardSearchContext
from chess.piece import (
    Piece, KingPiece, AttackEvent, AttackingEnemyKingException, AttackingFriendException, CombatantPiece,
    DoublyAttackingPrisonerException, NullAttackEventException, PieceAttackingItSelfException, PieceValidator,
    TravelActorValidator, TravelResourceValidator, UnregisteredTeamMemberException
)
from chess.piece.travel.attack.exception import (
    AttackingPieceMissingFromBoardException,
    EnemyNotInExpectedSquareException
)
from chess.system import ValidationResult, Validator
from chess.team import InconsistentHostageEntry


class AttackEventValidator(Validator[AttackEvent]):
    """"""
    
    @classmethod
    def validate(cls, candidate: Any) -> ValidationResult[AttackEvent]:
        """"""
        method = "AttackEventValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullAttackEventException(f"{method}: {NullAttackEventException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, AttackEvent):
                return ValidationResult.failure(TypeError(f"Expected an AttackEvent, got {type(candidate).__name__}"))
    
            event = cast(AttackEvent, candidate)
            actor_board_binding_validation = TravelActorValidator.validate(event.actor, event.execution_environment)
            if actor_board_binding_validation.is_failure():
                return ValidationResult.failure(actor_board_binding_validation.exception)
    
            resource_board_binding_validation = TravelResourceValidator.validate(
                event.resource,
                event.execution_environment
            )
            if resource_board_binding_validation.is_failure():
                return ValidationResult.failure(resource_board_binding_validation.exception)
            
            piece_validation = PieceValidator.validate(event.enemy_combatant)
            if piece_validation.is_failure():
                return ValidationResult.failure(piece_validation.exception)
            
            if event.actor == event.enemy_combatant:
                return ValidationResult.failure(
                    PieceAttackingItSelfException(PieceAttackingItSelfException.DEFAULT_MESSAGE)
                )
            
            if not event.actor.is_enemy(event.enemy_combatant):
                return ValidationResult.failure(
                    AttackingFriendException(f"{method}: {AttackingFriendException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(event.enemy_combatant, KingPiece):
                return ValidationResult.failure(
                    AttackingEnemyKingException(AttackingEnemyKingException.DEFAULT_MESSAGE)
                )
            
            if cast(CombatantPiece, event.enemy_combatant).captor is not None:
                return ValidationResult.failure(
                    DoublyAttackingPrisonerException(f"{method}: {DoublyAttackingPrisonerException.DEFAULT_MESSAGE}")
                )
            
            enemy_team = event.enemy_combatant.team
            if event.enemy_combatant not in enemy_team.roster:
                return ValidationResult.failure(
                    UnregisteredTeamMemberException(
                        f"{method}: Cannot attack enemy missing from team roster. There may be a data inconsistency."
                    )
                )
            
            actor_team = event.actor.team
            if event.enemy_combatant in actor_team.hostages:
                return ValidationResult.failure(
                    InconsistentHostageEntry(f"{method}: {InconsistentHostageEntry.DEFAULT_MESSAGE}")
                )
            
            enemy_combatant = cast(CombatantPiece, event.enemy_combatant)
            board = cast(Board, event.execution_environment)
            piece_search = BoardPieceSearch.search(
                board=board,
                search_context=BoardSearchContext(id=enemy_combatant.id)
            )
            if piece_search.is_empty():
                return ValidationResult.failure(
                    AttackingPieceMissingFromBoardException(
                        f"{method}: {AttackingPieceMissingFromBoardException.DEFAULT_MESSAGE}"
                    )
                )
            
            if piece_search.is_failure():
                return ValidationResult.failure(piece_search.exception)
            
            enemy_square_binding_validation = TravelResourceValidator.validate(event.destination_square, board)
            if enemy_square_binding_validation.is_failure():
                return ValidationResult.failure(enemy_square_binding_validation.exception)
            
            if event.enemy_square.occupant != event.enemy_combatant:
                return ValidationResult.failure(
                    EnemyNotInExpectedSquareException(f"{method}: {EnemyNotInExpectedSquareException.DEFAULT_MESSAGE}")
                )
         
            return ValidationResult.success(event)
        except Exception as e:
            return ValidationResult.failure(e)