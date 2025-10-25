# src/chess/piece/travel/occupation/notification/notification.py

"""
Module: `chess.piece.travel.occupation.notification.notification`
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""
from chess.piece.travel.promotion.transaction import PromotionTransaction
from chess.system import LoggingLevelRouter, TransactionResult, id_emitter
from chess.piece import (
    PromotionEvent, PromotionEventValidator, TravelTransaction, OccupationEvent, OccupationEventValidator,
    FailedActorPositionUpdateRolledBackException,
    FailedActorSquareVacationRolledBackException, FailedDestinationSquareOccupationRolledBackException
)

class OccupationTransaction(TravelTransaction[OccupationEvent]):
    """"""
    _event: OccupationEvent
    
    def __init__(self, event: OccupationEvent):
        super().__init__(event)
    
    @LoggingLevelRouter.monitor
    def execute(self) -> TransactionResult:
        method = "OccupationTransaction.execute"
        
        try:
            # Step 1: Ensure the travel will not have failure conditions, i.e, traveler is a hostage,
            # the enemy_square is empty.
            validation = OccupationEventValidator.validate(self.event)
            if validation.is_failure():
                return TransactionResult.errored(event_update=self.event, exception=validation.exception)
            
            # Step 2: Actor occupies enemy_square
            self.event.destination_square.occupant = self.event.actor
            
            """
            # Step 2.1:
            If Step 2 was successful actor_square and enemy_square should have the same occupant. Only checking
            enemy_square != traveler is not a sufficient success condition. If the traveler is not in both squares then
            rollback all the operations and return the rollback_exception.
            """
            if self.event.destination_square.occupant != self.event.actor_square.occupant:
                self.event.destination_square.occupant = None
                
                return TransactionResult.rolled_back(
                    event_update=self.event,
                    rollback_exception=FailedDestinationSquareOccupationRolledBackException(
                        f"{method}: {FailedDestinationSquareOccupationRolledBackException.DEFAULT_MESSAGE}"
                    )
                )
            
            # Step 3: Remove the traveler from their old square.
            self.event.actor_square.occupant = None
            
            """
            #Step 3.1
            Cannot guarantee that traveler's previous square is empty. So the success condition is:
                actor_previous_square.occupant != traveler.
            If the condition is not met then rollback the operations and return the rollback_exception.
            """
            if self.event.actor_square.occupant != self.event.actor:
                self.event.actor_square.occupant = self.event.actor
                self.event.destination_square.occupant = None
                
                # Send the error and last checkpoint in the result
                return TransactionResult.rolled_back(
                    event_update=self.event,
                    rollback_exception=FailedActorSquareVacationRolledBackException(
                        f"{method}: {FailedActorSquareVacationRolledBackException.DEFAULT_MESSAGE}"
                    )
                )
            
            self.event.actor.positions.push_coord(self.event.destination_square.coord)
            
            # If the push destination coord is not the traveler's current position rollback the operations,
            # then return the rollback_exception.
            if self.event.actor.current_position != self.event.destination_square.coord:
                self.event.actor.positions.undo_push()
                self.event.actor_square.occupant = self.event.actor
                self.event.destination_square.occupant = None
                
                # Send the error and last checkpoint in the result
                return TransactionResult.rolled_back(
                    event_update=self.event,
                    rollback_exception=FailedActorPositionUpdateRolledBackException(
                        f"{method}: {FailedActorPositionUpdateRolledBackException.DEFAULT_MESSAGE}"
                    )
                )
            
            self.event.actor.discoveries.clear()
            
            promotion_validation = PromotionEventValidator.validate(self.event)
            if promotion_validation.is_success():
                promotion_event = PromotionEvent(
                    parent=self.event,
                    id=id_emitter.event_id,
                    actor=self.event.actor,
                    actor_square=self.event.actor_square,
                    promotion_square=self.event.destination_square,
                    execution_environment=self.event.execution_environment,
                )
                return PromotionTransaction(promotion_event).execute()
            
            return TransactionResult.success(event_update=self.event)
        except Exception as e:
            return TransactionResult.errored(self.event, e)
