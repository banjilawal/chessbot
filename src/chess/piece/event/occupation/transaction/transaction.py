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
from chess.piece import OccupationEvent, OccupationEventValidator
from chess.piece.event.occupation.transaction.exception import (
    FailedActorPositionUpdateRollBackException, FailedActorSquareVacationRollBackException,
    FailedDestinationSquareOccupationRollBackException
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
        
        validation = OccupationEventValidator.validate(self._event)
        if validation.is_failure():
            return TransactionResult.failed(event_update=self._event, exception=validation.exception)
        
        self._event.destination_square.occupant = self._event.actor
        if self._event.destination_square.occupant != self._event.actor_square.occupant:
            self._event.destination_square.occupant = None
            return TransactionResult.rolled_back(
                event_update=self._event,
                exception=FailedDestinationSquareOccupationRollBackException(
                    f"{method}: {FailedDestinationSquareOccupationRollBackException.DEFAULT_MESSAGE}"
                )
            )
        
        self._event.actor_square.occupant = None
        if self._event.actor_square.occupant != self._event.actor:
            self._event.actor_square.occupant = self._event.actor
            self._event.destination_square.occupant = None
            return TransactionResult.rolled_back(
                event_update=self._event,
                exception=FailedActorSquareVacationRollBackException(
                    f"{method}: {FailedActorSquareVacationRollBackException.DEFAULT_MESSAGE}"
                )
            )
        
        self._event.actor.positions.push_coord(self._event.destination_square.coord)
        if self._event.actor.current_position != self._event.destination_square.coord:
            self._event.actor.positions.undo_push()
            self._event.actor_square.occupant = self._event.actor
            self._event.destination_square.occupant = None
            return TransactionResult.rolled_back(
                event_update=self._event,
                exception=FailedActorPositionUpdateRollBackException    (
                    f"{method}: {FailedActorPositionUpdateRollBackException.DEFAULT_MESSAGE}"
                )
            )
        
        return TransactionResult.success(event_update=self._event)