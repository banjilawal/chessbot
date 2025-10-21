"""
Module: transaction
Author: Banji Lawal
Created: 2025-10-01

Purpose:
  Implements the `AttackTransaction` class, responsible for capturing an enemy `CombatantPiece`

Contents:
  - `AttackTransaction:` Class responsible for AttackTransaction lifecycle.

Notes:
  This module is part of the chess.event.event.attack package.
  Exceptions raised during execution are defined in err.py.
"""
from chess.piece import (
    OccupationEvent, OccupationEventValidator, FailedActorPositionUpdateRolledBackException,
    FailedActorSquareVacationRolledBackException, FailedDestinationSquareOccupationRolledBackException
)
from chess.piece.event.travel_transaction import TravelTransaction
from chess.system import LoggingLevelRouter, TransactionResult


class OccupationTransaction(TravelTransaction):
    _event: OccupationEvent

    def __init__(self, event: OccupationEvent):
        super().__init__(event)

    @LoggingLevelRouter.monitor
    def execute(self) -> TransactionResult:
        method = "OccupationTransaction.execute"
        
        # Step 1: Ensure the event will not have failure conditions, i.e, actor is a hostage,
        # the destination_square is empty.
        validation = OccupationEventValidator.validate(self._event)
        if validation.is_failure():
            return TransactionResult.failed(event_update=self._event, exception=validation.exception)
        event_backup
        
        # Step 2: Actor occupies destination_square
        self._event.destination_square.occupant = self._event.actor
        
        """
        # Step 2.1:
        If Step 2 was successful actor_square and destination_square should have the same occupant. Only checking
        destination_square != actor is not a sufficient success condition. If the actor is not in both squares then
        rollback all the operations and return the exception.
        """
        if self._event.destination_square.occupant != self._event.actor_square.occupant:
            self._event.destination_square.occupant = None
            return TransactionResult.rolled_back(
                event_update=self._event,
                exception=FailedDestinationSquareOccupationRolledBackException(
                    f"{method}: {FailedDestinationSquareOccupationRolledBackException.DEFAULT_MESSAGE}"
                )
            )
        
        # Step 3: Remove the actor from their old square.
        self._event.actor_square.occupant = None
        
        """
        #Step 3.1
        Cannot guarantee that actor's previous square is empty. So the success condition is:
            actor_previous_square.occupant != actor.
        If the condition is not met then rollback the operations and return the exception.
        """
        if self._event.actor_square.occupant != self._event.actor:
            self._event.actor_square.occupant = self._event.actor
            self._event.destination_square.occupant = None
            return TransactionResult.rolled_back(
                event_update=self._event,
                exception=FailedActorSquareVacationRolledBackException(
                    f"{method}: {FailedActorSquareVacationRolledBackException.DEFAULT_MESSAGE}"
                )
            )
        
        self._event.actor.positions.push_coord(self._event.destination_square.coord)
        
        # If the push destination coord is not the actor's current position rollback the operations,
        # then return the exception.
        if self._event.actor.current_position != self._event.destination_square.coord:
            self._event.actor.positions.undo_push()
            self._event.actor_square.occupant = self._event.actor
            self._event.destination_square.occupant = None
            return TransactionResult.rolled_back(
                event_update=self._event,
                exception=FailedActorPositionUpdateRolledBackException    (
                    f"{method}: {FailedActorPositionUpdateRolledBackException.DEFAULT_MESSAGE}"
                )
            )
        
        return TransactionResult.success(event_update=self._event)