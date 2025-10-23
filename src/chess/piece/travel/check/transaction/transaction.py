""""
Module: chess.travel.travel.attack.notification
Author: Banji Lawal
Created: 2025-10-01
Version: 1.0.0

Purpose:
  Implements the `AttackTransaction` class, responsible for capturing an enemy `CombatantPiece`

Contents:
  - `AttackTransaction:` Class responsible for AttackTransaction lifecycle.

Notes:
"""

from chess.board import FailedPieceRemovalRolledBackException
from chess.piece import OldTravelTransaction
from chess.system import Transaction, TransactionResult, id_emitter
from chess.event import AttackEvent, OccupationTransaction, TransferEvent, AttackEventValidator
from chess.piece.event.attack.event.exception import SetCaptorRolledBackException, \
  EmptyDestinationSquareRolledBackException
from chess.piece.event.occupation.transaction import OccupationTransaction
from chess.team import AddEnemyHostageRolledBackException, RemoveTeamMemberRolledBackException


class CheckTransaction(Transaction[CheckEvent]):

  @staticmethod
  def execute(event: AttackEvent) -> TransactionResult:
    method = "AttackTransaction.execute"

    validation = AttackEventValidator.validate(event)
    if not validation.is_success():
      return TransactionResult(event, validation.exception)

    event.enemy_combatant.captor = event.actor
    if event.enemy_combatant.captor != event.actor:
      # Rollback all changes in reverse order
      event.enemy_combatant.captor = None

      # Send the notification indicating rollback
      return TransactionResult(
        event=event,
        was_rolled_back=True,
        exception=SetCaptorRolledBackException(
          f"{method}: {SetCaptorRolledBackException.DEFAULT_MESSAGE}"
        )
      )

    event.enemy_combatant.team.roster.remove(event.enemy_combatant)
    if event.enemy_combatant in event.enemy_combatant.team.roster:
      # Rollback all changes in reverse order
      event.enemy_combatant.captor = None

      # Send the notification indicating rollback
      return TransactionResult(
        event=event,
        was_rolled_back=True,
        exception=RemoveTeamMemberRolledBackException(
          f"{method}: {RemoveTeamMemberRolledBackException.DEFAULT_MESSAGE}"
        )
      )

    event.actor.team.hostages.append(event.enemy_combatant)
    if event.enemy_combatant not in event.actor.team.hostages:
      # Rollback all changes in reverse order
      event.enemy_combatant.team.add_to_roster(event.enemy_combatant)
      event.enemy_combatant.captor = None

      # Send the notification indicating rollback
      return TransactionResult(
        event=event,
        was_rolled_back=True,
        exception=AddEnemyHostageRolledBackException(
          f"{method}: {AddEnemyHostageRolledBackException.DEFAULT_MESSAGE}"
        )
      )

    context.board.pieces.remove(event.enemy_combatant)
    if event.enemy_combatant in event.board.pieces:
      # Rollback all changes in reverse order
      event.actor.team.hostages.remove(event.enemy_combatant)
      event.enemy_combatant.team.add_to_roster(event.enemy_combatant)
      event.enemy_combatant.captor = None

      # Send the notification indicating rollback
      return TransactionResult(
        event=event,
        was_rolled_back=True,
        exception=FailedPieceRemovalRolledBackException(
          f"{method}: {FailedPieceRemovalRolledBackException.DEFAULT_MESSAGE}"
        )
      )

    event.enemy_square.occupant = None
    if not event.enemy_square.occupant is None:
      # Rollback all changes in reverse order
      context.board.pieces.add(event.enemy_square.occupant)
      event.actor.team.hostages.remove(event.enemy_combatant)
      event.enemy_combatant.team.add_to_roster(event.enemy_combatant)
      event.enemy_combatant.captor = None

      # Send the notification indicating rollback
      return TransactionResult(
        event=event,
        was_rolled_back=True,
        exception=EmptyDestinationSquareRolledBackException(
          f"{method}: {EmptyDestinationSquareRolledBackException.DEFAULT_MESSAGE}"
        )
      )

    transfer_event = TransferEvent(
      parent=event,
      actor=event.actor,
      event_id=id_emitter.attack_id,
      actor_square=event.actor_square
    )
    return OccupationTransaction.execute(transfer_event, context)


