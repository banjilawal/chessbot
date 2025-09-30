"""
Module: executor
Author: Banji Lawal
Created: 2025-09-28

Purpose:
    Implements the `OccupationExecutor` class, which handles executing occupation
    directives in the chess engine. This includes moving pieces, capturing enemies,
    and coordinating rollback logic in case of inconsistencies or failed operations.

Contents:
    - `OccupationExecutor:` Main class responsible for executing occupation directives.
    - `_attack_enemy`: Static method for processing attacks on enemy pieces.
    - `_run_scan`: Static method for handling discoveries on occupied squares.
    - `_switch_squares`: Static method the transferring a piece to a different `Square`.

Notes:
    This module is part of the chess.transaction.occupation package.
    Exceptions raised during execution are defined in attack_exceptions.py and exception.py.
"""


from typing import cast

from chess.common import id_emitter

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


class OccupationTransaction(Transaction[OccupationEvent]):

    @staticmethod
    def execute(event: OccupationEvent, context: ExecutionContext) -> TransactionResult:
        method = "OccupationExecutor.execute_directive"
        op_result_id = id_emitter.op_result_id

        validation = OccupationEventValidator.validate(event)
        if not validation.is_success():
            return TransactionResult(op_result_id, event, validation.exception)

        search_result = BoardSearch.square_by_coord(coord=event.actor.current_position, board=context.board)
        if search_result.exception is not None:
            return TransactionResult(op_result_id, event, search_result.exception)

        if search_result.is_not_found():
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
        if not actor.is_enemy(destination_occupant) or (
            actor.is_enemy(destination_occupant) and isinstance(destination_occupant, KingPiece)
        ):
            return OccupationTransaction._run_scan(
                op_result_id=op_result_id,
                directive=ScanDirective(
                    actor=event.actor,
                    occupation_id=event.id,
                    scan_id=id_emitter.scan_id,
                    subject=destination_occupant,
                    destination_square=event.subject
                )
            )


        attack_validation = AttackValidator.validate(
            CaptureContext(piece=event.actor, enemy=destination_occupant, board=context.board)
        )
        if not attack_validation.is_success():
            return TransactionResult(op_result_id, event, attack_validation.exception)

        enemy_combatant = cast(CombatantPiece, attack_validation.payload.enemy)
        return OccupationTransaction._attack_enemy(
            op_result_id=op_result_id,
            directive=AttackDirective(
                board=context.board,
                actor=event.actor,
                enemy=enemy_combatant,
                occupation_id=event.id,
                attack_id=id_emitter.attack_id,
                actor_square=actor_square,
                destination_square=event.subject
            )


    @staticmethod
    def _switch_squares(op_result_id: int, directive: OccupationEvent, actor_square: Square) -> TransactionResult:
        """
        Transfers `Piece` occupying`actor_square` to `directive.destination_square` leaving `actor_square` empty.
        `OccupationExecutor.execute_directive` is the single entry point to `_switch_squares`. Before `_switch_squares`
        was called `execute_directive`: validated the parameters, handled exceptions, and confirmed
        `directive.destination_square` contained either
            * A friendly piece blocking `actor` from `destination_square`
            * An enemy king. Kings cannot be captured, only checked or checkmated.

        Args:
            - `op_result_id` (`int`): The `id` of the `OperationResult` passed to the caller.
            - `directive` (`OccupationDirective`): The `OccupationDirective` to be executed.
            - `actor_square` (`Square`): The `Square` occupied by `actor`.

        Returns:
        `OccupationResult` containing:
            - On success: A new `OccupationDirective` with the updated squares and `piece`.
            - On failure: The original `OccupationDirective`or verifying any rollbacks succeeded and the exception
                describing the failure.

        Raises:
        Errors raised will be about data and state inconsistencies OccupationException: Wraps any errors including:
            -

        Note:
        *   If the transaction fails, `OperationResult.was_rolled_back = True`
        """
        method = "OccupationExecutor._switch_squares"

        directive.subject.occupant = directive.actor
        if not directive.subject.occupant == directive.actor:
            # Rollback all changes in reverse order
            directive.subject.occupant = None

            # Send the result indicating rollback
            return TransactionResult(
                result_id=op_result_id,
                event=directive,
                was_rolled_back=True,
                exception=OccupationEventException(f"{method}: {OccupationEventException.DEFAULT_MESSAGE}"),
            )

        actor_square.occupant = None
        if actor_square.occupant == directive.actor:
            # Rollback all changes in reverse order
            actor_square.occupant = directive.actor
            directive.subject.occupant = None

            # Send the result indicating rollback
            return TransactionResult(
                result_id=op_result_id,
                event=directive,
                was_rolled_back=True,
                exception=OccupationEventException(f"{method}: {OccupationEventException.DEFAULT_MESSAGE}")
            )

        directive.actor.positions.push_coord(directive.subject.coord)
        if not directive.actor.current_position == directive.subject.coord:
            # Rollback all changes in reverse order
            directive.actor.positions.undo_push()
            actor_square.occupant = directive.actor
            directive.subject.occupant = None

            # Send the result indicating rollback
            return TransactionResult(
                result_id=op_result_id,
                event=directive,
                was_rolled_back=True,
                exception=OccupationEventException(f"{method}: {OccupationEventException.DEFAULT_MESSAGE}"),
            )

        return TransactionResult(
            result_id=op_result_id,
            event=OccupationEvent(id_emitter.event_id, directive.actor, directive.subject)
        )


    @staticmethod
    def _run_scan(op_result_id :int, directive: ScanDirective) -> TransactionResult:
        """
        Creates a new `Discovery` object for directive.observer which is blocked from moving to
        `destination_square` by `directive.subject`. The subject is either a friendly piece or an enemy `KingPiece`.
        `OccupationExecutor.execute_directive` is the single entry point to `_run_scan`. Validations, exception chains
        confirmed parameters ar are correct. No additional sanity checks are needed.

        Args
            - `op_result_id` (`int`): The `id` of the `OperationResult` passed to the caller.
            - `directive` (`ScanDirective`): The `ScanDirective` to execute.

        Returns:
        `OccupationResult` containing:
            - On success: A new `ScanDirective` object that containing updated `observer`. Observer will have
                a new `Discovery` instance inside `observer.discoveries`.
            - On failure: The original `ScanDirective` for verifying any rollbacks succeeded and the exception
                describing the failure.

        Raises:
        Errors raised will be about data and state inconsistencies OccupationException: Wraps any errors including:
            -
        Note:
        """
        method = "OccupationExecutor._run_scan"

        build_outcome = DiscoveryBuilder.build(observer=directive.observer, subject=directive.subject)
        if not build_outcome.is_success():
            return TransactionResult(op_result_id, directive, exception=build_outcome.exception)

        discovery = cast(Discovery, build_outcome.payload)
        if discovery not in directive.observer.discoveries.items:
            directive.observer.discoveries.record_discovery(discovery=discovery)

        if discovery not in directive.observer.discoveries.items:
            return TransactionResult(
                # There is nothing to actually do so there is no rollback because the discover was not added
                result_id=op_result_id,
                event=directive,
                was_rolled_back=True,
                exception=OccupationEventException(f"{method}: {OccupationEventException.DEFAULT_MESSAGE}"),
            )

        success_directive = ScanDirective(
            actor=directive.piece,
            subject=directive.subject,
            occupation_id=directive.id,
            scan_id=id_emitter.scan_id,
            destination_square=directive.subject
        )
        return TransactionResult(result_id=op_result_id, event=success_directive)


    @staticmethod
    def _attack_enemy(op_result_id: int, directive: AttackDirective) -> TransactionResult:

        method = "OccupationExecutor._attack_enemy"

        directive.enemy.captor = directive.piece
        if directive.enemy.captor != directive.piece:
            # Rollback all changes in reverse order
            directive.enemy.captor = None

            # Send the result indicating rollback
            return TransactionResult(
                result_id=op_result_id,
                event=directive,
                exception=OccupationEventException(f"{method}: {OccupationEventException.DEFAULT_MESSAGE}"),
                was_rolled_back=True
            )

        directive.enemy.team.roster.remove(directive.enemy)
        if directive.enemy in directive.enemy.team.roster:
            # Rollback all changes in reverse order
            directive.enemy.captor = None

            # Send the result indicating rollback
            return TransactionResult(
                result_id=op_result_id,
                event=directive,
                was_rolled_back=True,
                exception=RemoveTeamMemberRolledBackException(
                    f"{method}: {RemoveTeamMemberRolledBackException.DEFAULT_MESSAGE}"
                )
            )

        directive.piece.team.hostages.append(directive.enemy)
        if directive.enemy not in directive.piece.team.hostages:
            # Rollback all changes in reverse order
            directive.enemy.team.add_to_roster(directive.enemy)
            directive.enemy.captor = None

            # Send the result indicating rollback
            return TransactionResult(
                result_id=op_result_id,
                event=directive,
                was_rolled_back=True,
                exception=AddEnemyHostageRolledBackException(
                    f"{method}: {AddEnemyHostageRolledBackException.DEFAULT_MESSAGE}"
                )
            )

        directive.subject.occupant = None
        if directive.subject.occupant is not None:
            # Rollback all changes in reverse order
            directive.piece.team.hostages.remove(directive.enemy)
            directive.enemy.team.add_to_roster(directive.enemy)
            directive.enemy.captor = None

            # Send the result indicating rollback
            return TransactionResult(
                result_id=op_result_id,
                event=directive,
                was_rolled_back=True,
                exception=OccupationEventException(f"{method}: {OccupationEventException.DEFAULT_MESSAGE}")
            )

        directive.board.pieces.remove(directive.enemy)
        if directive.enemy in directive.board.pieces:
            # Rollback all changes in reverse order
            directive.subject.occupant = directive.enemy
            directive.piece.team.hostages.remove(directive.enemy)
            directive.enemy.team.add_to_roster(directive.enemy)
            directive.enemy.captor = None

            # Send the result indicating rollback
            return TransactionResult(
                result_id=op_result_id,
                event=directive,
                was_rolled_back=True,
                exception=BoardPieceRemovalRollbackException(
                    f"{method}: {BoardPieceRemovalRollbackException.DEFAULT_MESSAGE}"
                )
            )

        return OccupationTransaction._switch_squares(op_result_id, directive, directive.actor_square)

