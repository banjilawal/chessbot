"""
Module: occupation_executor
Author: Banji Lawal
Created: 2025-09-28
Purpose:
    Implements the OccupationExecutor class, which handles executing occupation
    directives in the chess engine. This includes moving pieces, capturing enemies,
    and coordinating rollback logic in case of inconsistencies or failed operations.

Contents:
    - OccupationExecutor: Main class responsible for executing occupation directives.
    - _attack_enemy: Static method for processing attacks on enemy pieces.
    - _record_discovery: Static method for handling discoveries on occupied squares.
    - Other helper functions for executing occupation directives safely.

Notes:
    This module is part of the chess.operation.occupation package.
    Exceptions raised during execution are defined in attack_exceptions.py and exception.py.
"""




from typing import cast

from chess.common import id_emitter

from chess.square import Square
from chess.board import Board
from chess.search import BoardSearch
from chess.piece import Piece, KingPiece, CombatantPiece, Discovery, NullPieceException
from chess.operation import OperationExecutor, Directive, ExecutionContext, OperationResult

from chess.operation.occupation.directive import OccupationDirective, ScanDirective, AttackDirective
from chess.operation.occupation.attack_exceptions import *
from chess.operation.occupation.exception import *
from chess.operation.occupation import (
    OccupationDirectiveValidator,
    InvalidOccupationDirectiveException,
    FatalBoardSearchException,
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


class OccupationExecutor(OperationExecutor):

    @staticmethod
    def execute_directive(directive: OccupationDirective, context: ExecutionContext) -> OperationResult:
        method = "OccupationExecutor.execute_directive"
        op_result_id = id_emitter.op_result_id

        validation = OccupationDirectiveValidator.validate(directive)
        if not validation.is_success():
            return OperationResult(op_result_id, directive, validation.exception)

        board = cast(Board, context.board)

        original_directive = cast(OccupationDirective, directive)
        piece = cast(Piece, original_directive.actor)
        target_square = cast(Square, original_directive.target)

        search_result = BoardSearch.square_by_coord(coord=piece.current_position, board=board)
        if search_result.exception is not None:
            raise search_result.exception

        if search_result.is_not_found():
            return OperationResult(
                op_result_id,
                original_directive,
                FatalBoardSearchException(f"{method}: {FatalBoardSearchException.DEFAULT_MESSAGE}")
            )
        source_square = cast(Square, search_result.payload)


        # validation = OccupationDirectiveValidator.validate(request)
        # if not validation.is_success():
        #     return validation.exception
        #
        # subject = cast(Piece, validation.request.actor)
        #
        # source_square = board.find_square_by_coord(subject.current_position)
        # target_square = cast(Square, request.target)

        if target_square.occupant is None:
            OccupationException._occuppy_
            return OccupationExecutor._occupy_empty_square(
                op_result_id=op_result_id,
                piece=piece,
                source_square=source_square,
                target_square=target_square,
                original_directive=original_directive,
                directive=directive
            )

        target_occupant = target_square.occupant


        if not piece.is_enemy(target_occupant):
            scan_directive = ScanDirective(
                occupation_id=original_directive.id,
                actor=original_directive.actor,
                target_square=original_directive.target,
                subject=target_occupant,
                scan_id=id_emitter.scan_id
            )
            return OccupationExecutor._run_scan(op_result_id=op_result_id, scan_directive=scan_directive)


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
        return OperationResult(op_result_id=op_result_id, directive=success_directive)

    @staticmethod
    def _occupy_empty_square(
        op_result_id: int,
        piece: Piece,
        source_square: Square,
        target_square: Square,
        original_directive: OccupationDirective,
        directive: Directive
    ) -> OperationResult:
        method = "OccupationExecutor._occupy_empty_square"

        if isinstance(piece, KingPiece):
            if piece.team.profile.is_in_check(board=source_square.board):
                return OperationResult(
                    op_result_id=op_result_id,
                    directive=original_directive,
                    exception=OccupationException(f"{method}: {OccupationException.DEFAULT_MESSAGE}"),
                    was_rolled_back=True
                )

        target_square.occupant = piece
        if not target_square.occupant == piece:
            # Rollback all changes
            target_square.occupant = None

            # Send the result indicating rollback
            return OperationResult(
                op_result_id=op_result_id,
                directive=original_directive,
                exception=OccupationException(f"{method}: {OccupationException.DEFAULT_MESSAGE}"),
                was_rolled_back=True
            )

        source_square.occupant = None
        if source_square.occupant == piece:
            # Rollback all changes
            target_square.occupant = None
            source_square.occupant = piece

            # Send the result indicating rollback
            return OperationResult(
                op_result_id=op_result_id,
                directive=original_directive,
                exception=OccupationException(f"{method}: {OccupationException.DEFAULT_MESSAGE}"),
                was_rolled_back=True
            )

        piece.positions.push_coord(target_square.coord)
        if not piece.current_position == target_square.coord:
            # Rollback all changes
            target_square.occupant = None
            source_square.occupant = piece
            piece.positions.undo_push()

            # Send the result indicating rollback
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
        return OperationResult(op_result_id=op_result_id, directive=success_directive)


    @staticmethod
    def _run_scan(
        op_result_id :int,
        # observer: Piece,
        # blocked_square: Square,
        scan_directive: ScanDirective
    ) -> OperationResult:
        """
        A destination occupied by a friendly is handled differently during an occupation operation than a
        scan operation. The difference is the conditions which raise exceptions. The friendly occupant is
        not provided directly to avoid mixing two args of the same type.

        Args
            `subject` (Piece): Records the encounter with a friendly at  `blocked_square`
            `blocked_square` (Square): The blocking friendly is extracted from here

         Returns:
             Result[T]: A Result object containing the validated payload if the Validator is 
                satisfied, NameValidationException otherwise.

        Raises:
            TypeError: if t is not int
            NullNameException: if t is null
            BlankNameException: if t only contains white space.
            ShortNameException: if t is shorter than MIN_NAME_LENGTH

            NameValidationException: Wraps any preceding team_exception 

        During an occupation operation the a square occupied by a friendly is handled differently
        than a `ScanOperation.        
        """
        method = "OccupationExecutor._run_scan"

        try:
            observer = cast(Piece, scan_directive.piece)
            subject = cast(Piece, scan_directive.subject)
            target_square = cast(Square, scan_directive.target)

            build_outcome = DiscoveryBuilder.build(observer=observer, subject=subject)
            if not build_outcome.is_success():
                return OperationResult(
                    op_result_id=op_result_id,
                    directive=scan_directive,
                    exception=build_outcome.exception
                )

            discovery = cast(Discovery, build_outcome.payload)
            if discovery not in observer.discoveries.items:
                observer.discoveries.record_discovery(discovery=discovery)

            if discovery not in observer.discoveries.items:
                return OperationResult(
                    # There is nothing to actually do so there is no rollback because the discovery was not added
                    op_result_id=op_result_id,
                    directive=scan_directive,
                    exception=OccupationException(f"{method}: {OccupationException.DEFAULT_MESSAGE}"),
                    was_rolled_back=True
                )

            success_directive = ScanDirective(
                actor=observer,
                target_square=target_square,
                subject=subject,
                occupation_id=id_emitter.directive_id,
                scan_id=id_emitter.scan_id
            )
        return OperationResult(op_result_id=op_result_id, directive=success_directive)


    @staticmethod
    def _attack_enemy(
        op_result_id: int,
        piece: Piece,
        source_square: Square,
        target_square: Square,
        board: Board,
        attack_directive: AttackDirective
    ) -> OperationResult:

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