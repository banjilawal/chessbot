# src/chess/piece/travel/blocked/validator.py

"""
Module: `chess.piece.travel.blocked.validator`
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import cast

from chess.system import IdValidator, LoggingLevelRouter, ValidationResult, Validator
from chess.piece import (
    ActorBlockingItsOwnSquareException, ActorSameAsBlockingFriendException, BlockingEvent,
    DiscoverySearch, DiscoverySearchContext, DiscoverySearchContextBuilder, NullBlockingEventException,
    OccupationBlockerIsEnemyException,
    PieceValidator,
    TravelActorValidator,
    TravelResourceValidator
)



class BlockingEventValidator(Validator[BlockingEvent]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: BlockingEvent) -> ValidationResult[BlockingEvent]:
        """"""
        method = "BlockingEventValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullBlockingEventException(f"{method}: {NullBlockingEventException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, BlockingEvent):
                return ValidationResult.failure(
                    exception=TypeError(f"{method} Expected an BlockingEvent, got {type(candidate).__name__}")
                )
            
            event = cast(BlockingEvent, candidate)
            
            id_validation = IdValidator.validate(event.id)
            if id_validation.is_failure():
                return ValidationResult.failure(id_validation.exception)
            
            actor_validation = TravelActorValidator.validate(event.actor, event.execution_environment)
            if actor_validation.is_failure():
                return ValidationResult.failure(actor_validation.exception)
            
            resource_validation = TravelResourceValidator.validate(event.blocked_square,event.execution_environment)
            if resource_validation.is_failure():
                return ValidationResult.failure(resource_validation.exception)
            
            if event.actor.current_position == event.blocked_square.coord:
                return ValidationResult.failure(
                    ActorBlockingItsOwnSquareException(f"{method}: {ActorBlockingItsOwnSquareException.DEFAULT_MESSAGE}")
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
            
            search_context_build_result = DiscoverySearchContextBuilder.build(piece_id=event.friend.id)
            if search_context_build_result.is_failure():
                return ValidationResult.failure(search_context_build_result.exception)
            search_context = cast(DiscoverySearchContext, search_context_build_result.payload)
            
            discovery_search = DiscoverySearch.search(owner=event.actor, search_context=search_context)
            if discovery_search.is_failure():
                return ValidationResult.failure(discovery_search.exception)
            
            if discovery_search.is_success():
                return ValidationResult.success(
                    DiscoveryAlreadyExistsException(f"{method}: {DiscoveryAlreadyExistsException.DEFAULT_MESSAGE}")
                )
            
            if event.actor == event.friend or :
                return ValidationResult.failure(
                    ActorSameAsBlockingFriendException(f"{method}: {ActorSameAsBlockingFriendException}")
                )
        
        except Exception as e:
            return ValidationResult(exception=e)