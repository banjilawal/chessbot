# src/chess/piece/travel/blocked/piece.py

"""
Module: `chess.piece.travel.blocked.validator`
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import cast

from chess.system import IdValidator, LoggingLevelRouter, ValidationResult, Validator
from chess.piece import (
    PieceBindingBoardValidator, ActorBlockingItsOwnSquareException, ActorSameAsBlockingFriendException, BlockingEvent,
    NullBlockingEventException, OccupationBlockerIsEnemyException, PieceValidator, TravelResourceValidator
)



class BlockingEventValidator(Validator[BlockingEvent]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: BlockingEvent) -> ValidationResult[BlockingEvent]:
        """"""
        method = "BlockingEventValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult(
                    exception=NullBlockingEventException(
                        f"{method}: {NullBlockingEventException.DEFAULT_MESSAGE}"
                    )
                )
            
            if not isinstance(candidate, BlockingEvent):
                return ValidationResult(
                    exception=TypeError(
                        f"{method} Expected an BlockingEvent, got {type(candidate).__name__}"
                    )
                )
            
            event = cast(BlockingEvent, candidate)
            
            id_validation = IdValidator.validate(event.id)
            if id_validation.is_failure():
                return ValidationResult(exception=id_validation.exception)
            
            actor_binding_validation = PieceBindingBoardValidator.validate(event.actor, event.execution_environment)
            if actor_binding_validation.is_failure():
                return ValidationResult(exception=actor_binding_validation.exception)
            
            resource_binding_validation = TravelResourceValidator.validate(
                event.blocked_square,
                event.execution_environment
            )
            
            if resource_binding_validation.is_failure():
                return ValidationResult(exception=resource_binding_validation.exception)
            
            if event.actor.current_position == event.blocked_square.coord:
                return ValidationResult(exception=ActorBlockingItsOwnSquareException(
                    f"{method}: {ActorBlockingItsOwnSquareException.DEFAULT_MESSAGE}"
                    )
                )
            
            blocker_validation = PieceValidator.validate(event.friend)
            if blocker_validation.is_failure():
                return ValidationResult(exception=blocker_validation.exception)
            
            if event.actor == event.friend:
                return ValidationResult(exception=ActorSameAsBlockingFriendException(
                    f"{method}: {ActorSameAsBlockingFriendException.DEFAULT_MESSAGE}"
                    )
                )
            
            if event.actor.is_enemy(event.friend):
                return ValidationResult(exception=OccupationBlockerIsEnemyException(
                    f"{method}: {OccupationBlockerIsEnemyException.DEFAULT_MESSAGE}"
                    )
                )
        
        except Exception as e:
            return ValidationResult(exception=e)