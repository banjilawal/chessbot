# src/chess/piece/travel/blocking/validator.py

"""
Module: `chess.piece.travel.blocking.validator`
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import cast

from chess.system import Validator, ValidationResult, IdValidator, LoggingLevelRouter
from chess.piece import (
    BlockingEvent, NullBlockingEventException, PieceValidator, BoardActorValidator, TravelResourceValidator,
    DiscoverySearchContextBuilder, DiscoverySearchContext, DiscoverySearch, ActorSameAsBlockerException,
    ActorBlockingOwnSquareException, EnemyCannotBeBlockerException, DiscoveryAlreadyExistsException
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
            
            actor_validation = BoardActorValidator.validate(
                actor=event.actor,
                environment=event.execution_environment
            )
            if actor_validation.is_failure():
                return ValidationResult.failure(actor_validation.exception)
            
            resource_validation = TravelResourceValidator.validate(
                resource=event.blocked_square,
                environment=event.execution_environment
            )
            if resource_validation.is_failure():
                return ValidationResult.failure(resource_validation.exception)
            
            if event.actor.current_position == event.blocked_square.coord:
                return ValidationResult.failure(
                    ActorBlockingOwnSquareException(f"{method}: {ActorBlockingOwnSquareException.DEFAULT_MESSAGE}")
                )
            
            blocker_validation = PieceValidator.validate(event.friend)
            if blocker_validation.is_failure():
                return ValidationResult(exception=blocker_validation.exception)
            
            if event.actor == event.friend:
                return ValidationResult(exception=ActorSameAsBlockerException(
                    f"{method}: {ActorSameAsBlockerException.DEFAULT_MESSAGE}")
                )
            
            if event.actor.is_enemy(event.friend):
                return ValidationResult(exception=EnemyCannotBeBlockerException(
                    f"{method}: {EnemyCannotBeBlockerException.DEFAULT_MESSAGE}")
                )
            
            context_build_result = DiscoverySearchContextBuilder.build(piece_id=event.friend.id)
            if context_build_result.is_failure():
                return ValidationResult.failure(context_build_result.exception)
            search_context = cast(DiscoverySearchContext, context_build_result.payload)
            
            discovery_search = DiscoverySearch.search(owner=event.actor, search_context=search_context)
            if discovery_search.is_failure():
                return ValidationResult.failure(discovery_search.exception)
            
            if discovery_search.is_success():
                return ValidationResult.success(
                    DiscoveryAlreadyExistsException(f"{method}: {DiscoveryAlreadyExistsException.DEFAULT_MESSAGE}")
                )
            
            if event.actor == event.friend:
                return ValidationResult.failure(
                    ActorSameAsBlockerException(f"{method}: {ActorSameAsBlockerException}")
                )
            
            return ValidationResult.success(event)
        
        except Exception as e:
            return ValidationResult(exception=e)