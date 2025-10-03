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

from chess.board import FailedPieceRemovalRolledBackException
from chess.system import id_emitter
from chess.event import AttackEvent, OccupationTransaction, TransferEvent, TransferEventValidator
from chess.event.occupation.attack.exception import EmptyDestinationSquareRolledBackException

from chess.square import Square
from chess.search import BoardSearch
from chess.piece import KingPiece, CombatantPiece, Discovery, DiscoveryBuilder
from chess.team import AddEnemyHostageRolledBackException
from chess.team.exception import RemoveTeamMemberRolledBackException
from chess.transaction import Transaction, ExecutionContext, TransactionResult, CaptureContext

from chess.transaction import AttackValidator
from chess.event.occupation import (
    OccupationEventValidator,
    OccupationSearchEventException,
    OccupationEvent,
    OccupationEventException,

    FriendlyFireException,
    AttackOnEmptySquareException,
    EnemyNotOnBoardException,
    NonCombatantTargetException,
    KingTargetException,
    AlreadyCapturedException,
    MissingFromRosterException,
    HostageTransferConflictException,

        # Rollback attack errors (dual inheritance)
    RosterRemovalRollbackException,
    HostageAdditionRollbackException,
    BoardPieceRemovalRollbackException,
)


class TransferTransaction(OccupationTransaction[TransferEvent]):

    @staticmethod
    def execute(event: TransferEvent, context: ExecutionContext) -> TransactionResult:
        method = "AttackTransaction.execute"

        validation = TransferEventValidator.validate(event)
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
                exception=SetCaptorRollBackException(
                    f"{method}: {SetCaptorRollBackException.DEFAULT_MESSAGE}"
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
            parent=event,
            actor=event.actor,
            event_id=id_emitter.attack_id,
            actor_square=event.actor_square
        )
        return Transfer
        event.subject.occupant = None
        if event.subject.occupant is not None:
            # Rollback all changes in reverse order
            event.actor.team.hostages.remove(event.enemy)
            event.enemy.team.add_to_roster(event.enemy)
            event.enemy.captor = None

            # Send the result indicating rollback
            return TransactionResult(
                result_id=op_result_id,
                event=event,
                was_rolled_back=True,
                exception=OccupationEventException(f"{method}: {OccupationEventException.DEFAULT_MESSAGE}")
            )



        return OccupationTransaction._switch_squares(op_result_id, event, event.actor_square)
        search_result = BoardSearch.square_by_coord(coord=event.actor.current_position, board=context.board)
        if search_result.exception is not None:
            return TransactionResult(op_result_id, event, search_result.exception)

        if search_result.is_empty():
            return TransactionResult(
                op_result_id,
                event,
                OccupationSearchEventException(f"{method}: {OccupationSearchEventException.DEFAULT_MESSAGE}")
            )
        actor_square = cast(Square, search_result.payload)

        if event.subject.occupant is None:
            return OccupationTransaction._switch_squares(op_result_id, event, actor_square)

        actor = event.actor
        destination_occupant = event.subject.occupant



        attack_validation = AttackValidator.validate(
            CaptureContext(piece=event.actor, enemy=destination_occupant, board=context.board)
        )
        if not attack_validation.is_success():
            return TransactionResult(op_result_id, event, attack_validation.exception)

        enemy_combatant = cast(CombatantPiece, attack_validation.payload.enemy)
        return OccupationTransaction._attack_enemy(
            op_result_id=op_result_id,
            event=AttackEvent(
                board=context.board,
                actor=event.actor,
                enemy=enemy_combatant,
                occupation_id=event.id,
                attack_id=id_emitter.attack_id,
                actor_square=actor_square,
                destination_square=event.subject
            )


    @staticmethod
    def _switch_squares(op_result_id: int, event: OccupationEvent, actor_square: Square) -> TransactionResult:
        """
        Transfers `Piece` occupying`actor_square` to `event.destination_square` leaving `actor_square` empty.
        `OccupationExecutor.execute_event` is the single entry point to `_switch_squares`. Before `_switch_squares`
        was called `execute_event`: validated the parameters, handled exceptions, and confirmed
        `event.destination_square` contained either
            * A friendly piece blocking `actor` from `destination_square`
            * An enemy king. Kings cannot be captured, only checked or checkmated.

        Args:
            - `op_result_id` (`int`): The `id` of the `OperationResult` passed to the caller.
            - `event` (`OccupationEvent`): The `OccupationEvent` to be executed.
            - `actor_square` (`Square`): The `Square` occupied by `actor`.

        Returns:
        `OccupationResult` containing:
            - On success: A new `OccupationEvent` with the updated squares and `piece`.
            - On failure: The original `OccupationEvent`or verifying any rollbacks succeeded and the exception
                describing the failure.

        Raises:
        Errors raised will be about data and state inconsistencies OccupationException: Wraps any errors including:
            -

        Note:
        *   If the transaction fails, `OperationResult.was_rolled_back = True`
        """
        method = "OccupationExecutor._switch_squares"

        event.subject.occupant = event.actor
        if not event.subject.occupant == event.actor:
            # Rollback all changes in reverse order
            event.subject.occupant = None

            # Send the result indicating rollback
            return TransactionResult(
                result_id=op_result_id,
                event=event,
                was_rolled_back=True,
                exception=OccupationEventException(f"{method}: {OccupationEventException.DEFAULT_MESSAGE}"),
            )

        actor_square.occupant = None
        if actor_square.occupant == event.actor:
            # Rollback all changes in reverse order
            actor_square.occupant = event.actor
            event.subject.occupant = None

            # Send the result indicating rollback
            return TransactionResult(
                result_id=op_result_id,
                event=event,
                was_rolled_back=True,
                exception=OccupationEventException(f"{method}: {OccupationEventException.DEFAULT_MESSAGE}")
            )

        event.actor.positions.push_coord(event.subject.coord)
        if not event.actor.current_position == event.subject.coord:
            # Rollback all changes in reverse order
            event.actor.positions.undo_push()
            actor_square.occupant = event.actor
            event.subject.occupant = None

            # Send the result indicating rollback
            return TransactionResult(
                result_id=op_result_id,
                event=event,
                was_rolled_back=True,
                exception=OccupationEventException(f"{method}: {OccupationEventException.DEFAULT_MESSAGE}"),
            )

        return TransactionResult(
            result_id=op_result_id,
            event=OccupationEvent(id_emitter.event_id, event.actor, event.subject)
        )


    @staticmethod
    def _run_scan(op_result_id :int, event: ScanEvent) -> TransactionResult:
        """
        Creates a new `Discovery` object for event.actor which is blocked from moving to
        `destination_square` by `event.enemy`. The enemy is either a friendly piece or an enemy `KingPiece`.
        `OccupationExecutor.execute_event` is the single entry point to `_run_scan`. Validations, exception chains
        confirmed parameters ar are correct. No additional sanity checks are needed.

        Args
            - `op_result_id` (`int`): The `id` of the `OperationResult` passed to the caller.
            - `event` (`ScanEvent`): The `ScanEvent` to execute.

        Returns:
        `OccupationResult` containing:
            - On success: A new `ScanEvent` object that containing updated `actor`. Observer will have
                a new `Discovery` instance inside `actor.discoveries`.
            - On failure: The original `ScanEvent` for verifying any rollbacks succeeded and the exception
                describing the failure.

        Raises:
        Errors raised will be about data and state inconsistencies OccupationException: Wraps any errors including:
            -
        Note:
        """
        method = "OccupationExecutor._run_scan"

        build_outcome = DiscoveryBuilder.build(observer=event.observer, subject=event.subject)
        if not build_outcome.is_success():
            return TransactionResult(op_result_id, event, exception=build_outcome.exception)

        discovery = cast(Discovery, build_outcome.payload)
        if discovery not in event.observer.discoveries.items:
            event.observer.discoveries.record_discovery(discovery=discovery)

        if discovery not in event.observer.discoveries.items:
            return TransactionResult(
                # There is nothing to actually do so there is no rollback because the discover was not added
                result_id=op_result_id,
                event=event,
                was_rolled_back=True,
                exception=OccupationEventException(f"{method}: {OccupationEventException.DEFAULT_MESSAGE}"),
            )

        success_event = ScanEvent(
            actor=event.actor,
            subject=event.subject,
            occupation_id=event.id,
            scan_id=id_emitter.scan_id,
            destination_square=event.subject
        )
        return TransactionResult(result_id=op_result_id, event=success_event)


    @staticmethod
    def _attack_enemy(op_result_id: int, event: AttackEvent) -> TransactionResult:


