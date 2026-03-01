""""
Module: logic.travel.travel.attack.notification
Author: Banji Lawal
Created: 2025-10-01
Version: 1.0.0

Purpose:
  Implements the `AttackTransaction` class, responsible for capturing an enemy `CombatantPiece`

Contents:
  - `AttackTransACTION:` Class responsible for AttackTransaction lifecycle.

Notes:
"""

from logic.board import FailedRemovalFromBoardRolledBackException
from logic.piece import KingCheckEvent, OldTravelTransaction, TravelTransaction
from logic.system import LoggingLevelRouter, Transaction, TransactionResult, id_emitter
from logic.event import AttackEvent, OccupationTransaction, TransferEvent, AttackEventValidator
from logic.token.event.attack.event.exception import SetCaptorRolledBackException, \
  EmptyDestinationSquareRolledBackException
from logic.token.event.occupation.transaction import OccupationTransaction
from logic.team import AddEnemyHostageRolledBackException, RemoveTeamMemberRolledBackException


class CheckTransaction(TravelTransaction[KingCheckEvent]):
  
  def __init__(self, event: KingCheckEvent):
    super().__init__(event)

  @LoggingLevelRouter.monitor
  def execute(self) -> TransactionResult:
    method = "AttackTransaction.execute"

    validation = AttackEventValidator.validate(self.event)
    if not validation.is_success():
      return TransactionResult(event, validation.exception)

    event.enemy_combatant.victor = event.actor
    if event.enemy_combatant.victor != event.actor:
      # Rollback all changes in reverse order
      event.enemy_combatant.victor = None

      # Send the notification indicating rollback
      return TransactionResult(
        event=event,
        was_rolled_back=True,
        exception=SetCaptorRolledBackException(
          f"{method}: {SetCaptorRolledBackException.MSG}"
        )
      )

    event.enemy_combatant.team_name.roster.remove(event.enemy_combatant)
    if event.enemy_combatant in event.enemy_combatant.team_name.roster:
      # Rollback all changes in reverse order
      event.enemy_combatant.victor = None

      # Send the notification indicating rollback
      return TransactionResult(
        event=event,
        was_rolled_back=True,
        exception=RemoveTeamMemberRolledBackException(
          f"{method}: {RemoveTeamMemberRolledBackException.MSG}"
        )
      )

    event.actor.team_name.hostages.append(event.enemy_combatant)
    if event.enemy_combatant not in event.actor.team_name.hostages:
      # Rollback all changes in reverse order
      event.enemy_combatant.team_name.add_to_roster(event.enemy_combatant)
      event.enemy_combatant.victor = None

      # Send the notification indicating rollback
      return TransactionResult(
        event=event,
        was_rolled_back=True,
        exception=AddEnemyHostageRolledBackException(
          f"{method}: {AddEnemyHostageRolledBackException.MSG}"
        )
      )

    context.board.pieces.remove(event.enemy_combatant)
    if event.enemy_combatant in event.board.pieces:
      # Rollback all changes in reverse order
      event.actor.team_name.hostages.remove(event.enemy_combatant)
      event.enemy_combatant.team_name.add_to_roster(event.enemy_combatant)
      event.enemy_combatant.victor = None

      # Send the notification indicating rollback
      return TransactionResult(
        event=event,
        was_rolled_back=True,
        exception=FailedRemovalFromBoardRolledBackException(
          f"{method}: {FailedRemovalFromBoardRolledBackException.MSG}"
        )
      )

    event.enemy_square.occupant = None
    if not event.enemy_square.occupant is None:
      # Rollback all changes in reverse order
      context.board.pieces.add_member(event.enemy_square.occupant)
      event.actor.team_name.hostages.remove(event.enemy_combatant)
      event.enemy_combatant.team_name.add_to_roster(event.enemy_combatant)
      event.enemy_combatant.victor = None

      # Send the notification indicating rollback
      return TransactionResult(
        event=event,
        was_rolled_back=True,
        exception=EmptyDestinationSquareRolledBackException(
          f"{method}: {EmptyDestinationSquareRolledBackException.MSG}"
        )
      )

    transfer_event = TransferEvent(
      parent=event,
      actor=event.actor,
      event_id=id_emitter.attack_id,
      actor_square=event.actor_square
    )
    return OccupationTransaction.execute(transfer_event, context)


