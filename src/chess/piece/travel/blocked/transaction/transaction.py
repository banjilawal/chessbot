"""
Module: notification
Author: Banji Lawal
Created: 2025-10-01
"""

from typing import cast

from chess.piece import (
    BlockingEventValidator, Discovery, DiscoveryBuilder, BlockingEvent, DiscoverySearch,
    DiscoverySearchContext, DiscoverySearchContextBuilder, TravelTransaction
)
from chess.system import ExecutionContext, TransactionResult
from chess.piece.discover.exception import AddingValidDiscoveryFailedException
from chess.event import (
    ScanEvent, OccupationTransaction, ScanTransactionException, OccupationEventException, ScanEventValidator
)

from chess.team import PieceSearchContextBuilder


class FriendBlockingTransaction(TravelTransaction[BlockingEvent]):
    
    @staticmethod
    def execute(event: BlockingEvent) -> TransactionResult:
        """
        # ACTION:
        Verify the `candidate` is a valid ID. The Application requires
        1. Candidate is not null.
        2. Is a positive integer.
    
        # PARAMETERS:
            * `candidate` (`int`): the id.
    
        # RETURNS:
        `ValidationResult[str]`: A `ValidationResult` containing either:
            `'payload'` (`it`) - A `str` meeting the `ChessBot` standard for IDs.
            `exception` (`Exception`) - An exception detailing which naming rule was broken.
    
        # RAISES:
        `InvalidIdException`: Wraps any specification violations including:
            * `TypeError`: if candidate is not an `int`
            * `IdNullException`: if candidate is null
            * `NegativeIdException`: if candidate is negative `
        """
        method = "OccupationTransaction.execute"
        
        try:
            event_validation = BlockingEventValidator.validate(event=event)
            if event_validation.is_failure():
                return TransactionResult.failed(event_validation.exception)
            
            event.actor.discoveries.append(Discovery(event.friend))
            
            context_build_result =
            search_result = DiscoverySearch.search(data_owner=event.actor, search_context=search_context)
            if search_result.is_failure():
                return TransactionResult.failed(search_result.exception)
            
            if search_result.is_empty():
                return TransactionResult.failed(
                    AddingValidDiscoveryFailedException(
                        f"{method}: {AddingValidDiscoveryFailedException.DEFAULT_MESSAGE}"
                        )
                )
            
            return TransactionResult.success(event)
        
        except Exception as e:
            raise TransactionResult.failed(e)
