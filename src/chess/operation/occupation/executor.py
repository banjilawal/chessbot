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
    This module is part of the chess.operation.occupation package.
    Exceptions raised during execution are defined in attack_exceptions.py and exception.py.
"""


from typing import cast

from chess.common import id_emitter

from chess.square import Square
from chess.board import Board
from chess.search import BoardSearch
from chess.piece import Piece, KingPiece, CombatantPiece, Discovery, DiscoveryBuilder
from chess.operation import OperationExecutor, ExecutionContext, OperationResult

from chess.operation.occupation.directive import OccupationDirective, ScanDirective, AttackDirective
from chess.operation.occupation.attack_exceptions import *
from chess.operation.occupation.exception import *
from chess.operation.occupation import (
    OccupationDirectiveValidator,
    InvalidOccupationDirectiveException,
    OccupationSearchException,
    OccupationDirective,
    OccupationException,

    UnexpectedNullEnemyException,
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
    SquareOccupationRollbackException,
    SourceSquareRollbackException,
    PositionUpdateRollbackException,
)


class OccupationExecutor(OperationExecutor[OccupationDirective]):

    @staticmethod
    def execute_directive(directive: OccupationDirective, context: ExecutionContext) -> OperationResult:
        method = "OccupationExecutor.execute_directive"
        op_result_id = id_emitter.op_result_id

        validation = OccupationDirectiveValidator.validate(directive)
        if not validation.is_success():
            return OperationResult(op_result_id, directive, validation.exception)


        search_result = BoardSearch.square_by_coord(coord=directive.piece.current_position, board=context.board)
        if search_result.exception is not None:
            return OperationResult(op_result_id, directive, search_result.exception)

        if search_result.is_not_found():
            return OperationResult(
                op_result_id,
                directive,
                OccupationSearchException(f"{method}: {OccupationSearchException.DEFAULT_MESSAGE}")
            )
        source_square = cast(Square, search_result.payload)

        if directive.destination_square.occupant is None:
            return OccupationExecutor._switch_squares(op_result_id, directive, source_square)

        attacker = directive.piece
        destination_occupant = directive.destination_square.occupant

        if not attacker.is_enemy(destination_occupant) or (
            attacker.is_enemy(destination_occupant) and isinstance(destination_occupant, KingPiece)
        ):
            return OccupationExecutor._run_scan(
                op_result_id=op_result_id,
                directive=ScanDirective(
                    actor=directive.piece,
                    occupation_id=directive.id,
                    scan_id=id_emitter.scan_id,
                    subject=destination_occupant,
                    destination_square=directive.destination_square
                )
            )


        if attacker.is_enemy(destination_occupant) and isinstance(destination_occupant, CombatantPiece):
            return OccupationExecutor._attack_enemy(
                op_result_id=op_result_id,
                directive=AttackDirective(
                    actor=directive.piece,
                    enemy=destination_occupant,
                    occupation_id=directive.id,
                    attack_id=id_emitter.attack_id,
                    source_square=source_square,
                    destination_square=directive.destination_square
                )
            )


        if target_occupant is not None and not piece.is_enemy(target_occupant):
            return OccupationExecutor._run_scan(
                op_result_id=op_result_id,
                observer=piece,
                original_directive=original_directive,
                blocked_square=target_square
            )


        if target_occupant is not None and piece.is_enemy(target_occupant):
            OccupationExecutor._attack_enemy(directive, piece, target_square)
        #
        #
        # if event == Event.ATTACK:
        #     enemy = OccupationExecutor._attack_stream(subject, target_square)

        target_square.occupant = piece
        source_square.occupant = None
        piece.positions.push_coord(target_square.coord)

        if piece.current_position == target_square.coord and not source_square.occupant == piece:
            piece.positions.undo_push()
            target_square.occupant = None
            source_square.occupant = piece
            return OperationResult(
                op_result_id=op_result_id,
                directive=directive,
                exception=OccupationException(f"{method}: {OccupationException.DEFAULT_MESSAGE}"),
                was_rolled_back=True
            )

        success_directive = OccupationDirective(
            occupation_id=id_emitter.directive_id,
            actor=piece,
            target=target_square
        )
        return OperationResult(result_id=op_result_id, directive=success_directive)


    @staticmethod
    def _switch_squares(op_result_id: int, directive: OccupationDirective, source_square: Square) -> OperationResult:
        """
        Transfers `Piece` occupying`source_square` to `directive.destination_square` leaving `source_square` empty.
        `OccupationExecutor.execute_directive` is the single entry point to `_switch_squares`. Before `_switch_squares`
        was called `execute_directive`: validated the parameters, handled exceptions, and confirmed
        `directive.destination_square` contained either
            * A friendly piece blocking `actor` from `destination_square`
            * An enemy king. Kings cannot be captured, only checked or checkmated.

        Args:
            - `op_result_id` (`int`): The `id` of the `OperationResult` passed to the caller.
            - `directive` (`OccupationDirective`): The `OccupationDirective` to be executed.
            - `source_square` (`Square`): The `Square` occupied by `actor`.

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

        directive.destination_square.occupant = directive.piece
        if not directive.destination_square.occupant == directive.piece:
            # Rollback all changes
            directive.destination_square.occupant = None

            # Send the result indicating rollback
            return OperationResult(
                result_id=op_result_id,
                directive=directive,
                was_rolled_back=True,
                exception=OccupationException(f"{method}: {OccupationException.DEFAULT_MESSAGE}"),
            )

        source_square.occupant = None
        if source_square.occupant == directive.piece:
            # Rollback all changes
            source_square.occupant = directive.piece
            directive.destination_square.occupant = None

            # Send the result indicating rollback
            return OperationResult(
                result_id=op_result_id,
                directive=directive,
                was_rolled_back=True,
                exception=OccupationException(f"{method}: {OccupationException.DEFAULT_MESSAGE}")
            )

        directive.piece.positions.push_coord(directive.destination_square.coord)
        if not directive.piece.current_position == directive.destination_square.coord:
            # Rollback all changes
            directive.piece.positions.undo_push()
            source_square.occupant = directive.piece
            directive.destination_square.occupant = None

            # Send the result indicating rollback
            return OperationResult(
                result_id=op_result_id,
                directive=directive,
                was_rolled_back=True,
                exception=OccupationException(f"{method}: {OccupationException.DEFAULT_MESSAGE}"),
            )

        return OperationResult(
            result_id=op_result_id,
            directive=OccupationDirective(id_emitter.occupation_id, directive.piece, directive.destination_square)
        )


    @staticmethod
    def _run_scan(op_result_id :int, directive: ScanDirective) -> OperationResult:
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
            return OperationResult(op_result_id, directive, exception=build_outcome.exception)

        discovery = cast(Discovery, build_outcome.payload)
        if discovery not in directive.observer.discoveries.items:
            directive.observer.discoveries.record_discovery(discovery=discovery)

        if discovery not in directive.observer.discoveries.items:
            return OperationResult(
                # There is nothing to actually do so there is no rollback because the discovery was not added
                result_id=op_result_id,
                directive=directive,
                was_rolled_back=True,
                exception=OccupationException(f"{method}: {OccupationException.DEFAULT_MESSAGE}"),
            )

        success_directive = ScanDirective(
            actor=directive.piece,
            subject=directive.subject,
            occupation_id=directive.id,
            scan_id=id_emitter.scan_id,
            destination_square=directive.destination_square
        )
        return OperationResult(result_id=op_result_id, directive=success_directive)


    @staticmethod
    def _attack_enemy(op_result_id: int, directive: AttackDirective) -> OperationResult:

        method = "OccupationExecutor._attack_enemy"
        enemy = target_square.occupant

        if enemy is None:
            return OperationResult(
                op_result_id=op_result_id,
                directive=original_directive,
                exception=UnexpectedNullEnemyException(
                    f"{method}: {UnexpectedNullEnemyException.DEFAULT_MESSAGE}"
                )
            )


        if not piece.is_enemy(enemy):
            return OperationResult(
                op_result_id=op_result_id,
                directive=original_directive,
                exception=FriendlyFireException(
                    f"{method}: {FriendlyFireException.DEFAULT_MESSAGE}"
                )
            )

        if enemy.positions.is_empty():
            return OperationResult(
                op_result_id=op_result_id,
                directive=original_directive,
                exception=AttackOnEmptySquareException(
                    f"{method}: {AttackOnEmptySquareException.DEFAULT_MESSAGE}"
                )
            )

        if enemy not in board.pieces:
            return OperationResult(
                op_result_id=op_result_id,
                directive=original_directive,
                exception=EnemyNotOnBoardException(
                    f"{method}: {EnemyNotOnBoardException.DEFAULT_MESSAGE}"
                )
            )

        if not isinstance(enemy, CombatantPiece):
            return OperationResult(
                op_result_id=op_result_id,
                directive=original_directive,
                exception=KingTargetException(
                    f"{method}: {KingTargetException.DEFAULT_MESSAGE}"
                )
            )

        if enemy.captor is not None:
            return OperationResult(
                op_result_id=op_result_id,
                directive=original_directive,
                exception=AlreadyCapturedException(
                    f"{method}: {AlreadyCapturedException.DEFAULT_MESSAGE}"
                )
            )

        enemy_team = enemy.team
        if enemy not in enemy_team.roster:
            return OperationResult(
                op_result_id=op_result_id,
                directive=original_directive,
                exception=MissingFromRosterException(
                    f"{method}: {MissingFromRosterException.DEFAULT_MESSAGE}"
                )
            )

        if enemy in piece.team.hostages:
            return OperationResult(
                op_result_id=op_result_id,
                directive=original_directive,
                exception=HostageTransferConflictException(
                    f"{method}: {HostageTransferConflictException.DEFAULT_MESSAGE}"
                )
            )

        enemy.captor = piece
        enemy_team.roster.remove(enemy)

        if enemy in enemy_team.roster:
            # Rollback all changes
            enemy.captor = None

            # Send the result indicating rollback
            return OperationResult(
                op_result_id=op_result_id,
                directive=original_directive,
                exception=RosterRemovalRollbackException(
                    f"{method}: {RosterRemovalRollbackException.DEFAULT_MESSAGE}"
                ),
                was_rolled_back=True
            )

        piece.team.hostages.append(enemy)
        if enemy not in piece.team.hostages:
            # Rollback all changes
            enemy.captor = None
            enemy_team.roster.append(enemy)

            # Send the result indicating rollback
            return OperationResult(
                op_result_id=op_result_id,
                directive=original_directive,
                exception=HostageAdditionRollbackException(
                    f"{method}: {HostageAdditionRollbackException.DEFAULT_MESSAGE}"
                ),
                was_rolled_back=True
            )

        board.pieces.remove(enemy)
        if enemy in board.pieces:
            # Rollback all changes
            enemy.captor = None
            enemy_team.roster.append(enemy)
            piece.team.hostages.remove(enemy)

            # Send the result indicating rollback
            return OperationResult(
                op_result_id=op_result_id,
                directive=original_directive,
                exception=BoardPieceRemovalRollbackException(
                    f"{method}: {BoardPieceRemovalRollbackException.DEFAULT_MESSAGE}"
                ),
                was_rolled_back=True
            )


        target_square.occupant = piece
        if not target_square.occupant == piece:
            # Rollback all changes
            enemy.captor = None
            enemy_team.roster.append(enemy)
            piece.team.hostages.remove(enemy)
            board.pieces.append(enemy)
            target_square.occupant = enemy

            # Send the result indicating rollback
            return OperationResult(
                op_result_id=op_result_id,
                directive=original_directive,
                exception=SquareOccupationRollbackException(
                    f"{method}: {SquareOccupationRollbackException.DEFAULT_MESSAGE}"
                ),
                was_rolled_back=True
            )

        source_square.occupant = None
        if source_square.occupant == piece:
            # Rollback all changes
            enemy.captor = None
            enemy_team.roster.append(enemy)
            piece.team.hostages.remove(enemy)
            board.pieces.append(enemy)
            target_square.occupant = enemy
            source_square.enemy = piece

            # Send the result indicating rollback
            return OperationResult(
                op_result_id=op_result_id,
                directive=original_directive,
                exception=SourceSquareRollbackException(
                    f"{method}: {SourceSquareRollbackException.DEFAULT_MESSAGE}"
                ),
                was_rolled_back=True
            )

        piece.positions.push_coord(target_square.coord)
        if not target_square.coord == piece.current_position:
            # Rollback all changes
            enemy.captor = None
            enemy_team.roster.append(enemy)
            piece.team.hostages.remove(enemy)
            board.pieces.append(enemy)
            target_square.occupant = enemy
            source_square.enemy = piece
            piece.positions.undo_push()

            # Send the result indicating rollback
            return OperationResult(
                op_result_id=op_result_id,
                directive=original_directive,
                exception=PositionUpdateRollbackException(
                    f"{method}: {PositionUpdateRollbackException.DEFAULT_MESSAGE}"
                ),
                was_rolled_back=True
            )

        success_directive = OccupationDirective(
            occupation_id=id_emitter.directive_id,
            actor=piece,
            target=target_square
        )

        return OperationResult(
            op_result_id=id_emitter.op_result_id,
            directive=success_directive,
        )


    @staticmethod
    def validate_enemy(piece: Piece, enemy: CombatantPiece) -> Result[CombatatntPiece]: