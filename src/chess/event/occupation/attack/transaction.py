"""
Module: transaction
Author: Banji Lawal
Created: 2025-10-01

Purpose:
    Implements the `AttackTransaction` class, responsible for capturing an enemy `CombatantPiece`

Contents:
    - `AttackTransaction:` Class responsible for AttackTransaction lifecycle.

Notes:
    This module is part of the chess.event.occupation.attack package.
    Exceptions raised during execution are defined in exception.py.
"""


from typing import cast

from chess.common import ExecutionContext, TransactionResult
from chess.event import AttackEvent, OccupationTransaction
from chess.event.occupation.attack.exception import SetCaptorRolledBackException


class AttackTransaction(OccupationTransaction[AttackEvent]):

    @staticmethod
    def execute(event: AttackEvent, context: ExecutionContext) -> TransactionResult:
        method = "AttackTransaction.execute"

        validation = AttackEventValidation.validate(event, context)
        if not validation.is_success():
            return TransactionResult(event, validation.exception)

        event.enemy.captor = event.actor
        if event.enemy.captor != event.actor:
            # Rollback all changes in reverse order
            event.enemy.captor = None

            # Send the result indicating rollback
            return TransactionResult(
                event=event,
                was_rolled_back=True,
                exception=SetCaptorRolledBackException(
                    f"{method}: {SetCaptorRolledBackException.DEFAULT_MESSAGE}"
                )
            )

        event.enemy.team.roster.remove(event.enemy)
        if event.enemy in event.enemy.team.roster:
            # Rollback all changes in reverse order
            event.enemy.captor = None

            # Send the result indicating rollback
            return TransactionResult(
                event=event,
                was_rolled_back=True,
                exception=RemoveTeamMemberRolledBackException(
                    f"{method}: {RemoveTeamMemberRolledBackException.DEFAULT_MESSAGE}"
                )
            )

        event.actor.team.hostages.append(event.enemy)
        if event.enemy not in event.actor.team.hostages:
            # Rollback all changes in reverse order
            event.enemy.team.add_to_roster(event.enemy)
            event.enemy.captor = None

            # Send the result indicating rollback
            return TransactionResult(
                event=event,
                was_rolled_back=True,
                exception=AddEnemyHostageRolledBackException(
                    f"{method}: {AddEnemyHostageRolledBackException.DEFAULT_MESSAGE}"
                )
            )

        event.board.pieces.remove(event.enemy)
        if event.enemy in event.board.pieces:
            # Rollback all changes in reverse order
            event.actor.team.hostages.remove(event.enemy)
            event.enemy.team.add_to_roster(event.enemy)
            event.enemy.captor = None

            # Send the result indicating rollback
            return TransactionResult(
                event=event,
                was_rolled_back=True,
                exception=FailedPieceRemovalRolledBackException(
                    f"{method}: {FailedPieceRemovalRolledBackException.DEFAULT_MESSAGE}"
                )
            )

        event.destination_square.occupant = None
        if not event.destination_square.occupant is None:
            # Rollback all changes in reverse order
            event.board.pieces.add(event.destination_square.occupant)
            event.actor.team.hostages.remove(event.enemy)
            event.enemy.team.add_to_roster(event.enemy)
            event.enemy.captor = None

            # Send the result indicating rollback
            return TransactionResult(
                event=event,
                was_rolled_back=True,
                exception=EmptyDestinationSquareRolledBackException(
                    f"{method}: {EmptyDestinationSquareRolledBackException.DEFAULT_MESSAGE}"
                )
            )

        transfer_event = TransferEvent(
            # parent=event,
            actor=event.actor,
            event_id=id_emitter.attack_id,
            actor_square=event.actor_square
        )
        return TransferTransaction.execute(transfer_event, context)


