"""
Module: notification
Author: Banji Lawal
Created: 2025-10-01
"""

from typing import cast

from chess.system import TransactionResult, LoggingLevelRouter
from chess.piece import (
    BlockingEvent, BlockingEventValidator, TravelTransaction, Discovery, DiscoverySearch,
    DiscoverySearchContextBuilder, DiscoverySearchContext, FailedDiscoveryAdditionRolledBackException
)


class BlockedPathTransaction(TravelTransaction[BlockingEvent]):
    
    def __init__(self, event: BlockingEvent):
        super().__init__(event)


    @LoggingLevelRouter.monitor
    def execute(self) -> TransactionResult:
        """
        # ACTION:
        Verify the `candidate` is a valid ID. The Application requires
        1. Candidate is not validation.
        2. Is a positive integer.
    
        # PARAMETERS:
            * `candidate` (`int`): the visitor_id.
    
        # RETURNS:
        `ValidationResult[str]`: A `ValidationResult` containing either:
            `'payload'` (`it`) - A `str` meeting the `ChessBot` standard for IDs.
            `rollback_exception` (`Exception`) - An rollback_exception detailing which naming rule was broken.
    
        # RAISES:
        `InvalidIdException`: Wraps any specification violations including:
            * `TypeError`: if candidate is not an `int`
            * `IdNullException`: if candidate is validation
            * `NegativeIdException`: if candidate is negative `
        """
        method = "OccupationTransaction.execute"
        
        try:
            event_validation = BlockingEventValidator.validate(event=self.event)
            if event_validation.is_failure():
                return TransactionResult.errored(
                    event_update=self.event,
                    exception=event_validation.exception
                )
            
            self.event.actor.discoveries.append(Discovery(self.event.friend))
            
            context_build = DiscoverySearchContextBuilder.build(piece_id=self.event.friend.visitor_id)
            if context_build.is_failure():
                return TransactionResult.errored(
                    event_update=self.event,
                    exception=context_build.exception
                )
            
            search_context = cast(DiscoverySearchContext, context_build.payload)
            search_result = DiscoverySearch.search(data_owner=self.event.actor, search_context=search_context)
            
            if search_result.is_failure():
                return TransactionResult.rolled_back(
                    event_update=self.event,
                    rollback_exception=FailedDiscoveryAdditionRolledBackException(search_result.exception)
                )
            
            if search_result.is_empty():
                return TransactionResult.rolled_back(
                    event_update=self.event,
                    rollback_exception=FailedDiscoveryAdditionRolledBackException(
                        f"{method}: {FailedDiscoveryAdditionRolledBackException.DEFAULT_MESSAGE}"
                    )
                )
            
            return TransactionResult.success(self.event)
        except Exception as e:
            return TransactionResult.errored(e)
